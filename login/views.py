from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import *

#用户登录注册函数
# Create your views here.
def loginViews(request):
    if request.method == "GET":
        return render(request,'login.html')
    elif request.method == "POST":
        types = request.POST['to']
        print(types)
        if types == 'log':
            uname = request.POST['username']
            upwd = request.POST['p']
            print('登录账号为%r,密码为%r' % (uname,upwd))
            if len(Userinfo.objects.filter(username=uname).all()):
                password = Userinfo.objects.get(username=uname).password
                image = Userinfo.objects.get(username=uname).userimage
                print('数据库密码:',password)
                print('头像地址:',image)
                if upwd == password:
                    print('有该账号')
                    if image:
                        request.session['image'] = image
                    else:
                        request.session['image'] = "/static/tou.png"
                    request.session['uname'] = uname
                    resp = redirect('/')
                    resp.set_cookie('uname',uname,60*60)
                    print('cookie是:',request.COOKIES)
                    return resp
                else:
                    print('密码错误')
                    dic = {'zt':'  密码错误!'}
                    return render(request,'login.html',dic)
            else:
                return render(request,'login.html')
        else:
            uname = request.POST['user']
            print('注册的时候')
            if not len(Userinfo.objects.filter(username=uname).all()):
                upwd = request.POST['passwd']
                uphone = request.POST['phone']
                print("注册")
                print(uname,upwd,uphone,sep='--')
                user = Userinfo()
                user.password = upwd
                user.username = uname
                user.phone = uphone
                user.save()
                request.session['image'] = "/static/tou.png"
                request.session['uname'] = uname
                resp = redirect('/')
                resp.set_cookie('uname', uname, 60*60)
                print('注册成功')
                return resp
            else:
                return render(request,'login.html',{'zt':"注册失败!"})

#异步加载处理函数
def ajaxViews(request):
    data = request.POST['data']
    print(data)
    if not len(Userinfo.objects.filter(username=data).all()):
        print('没有该账号！')
        return JsonResponse({'data':"no"})
    else:
        return JsonResponse({'data':'yes'})

#退出登录函数
def logoutViews(request):
    del request.session['uname']
    del request.session['image']
    resp = redirect('/')
    resp.delete_cookie('uname')
    print('删除session成功!')
    return resp
