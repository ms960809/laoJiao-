from django.shortcuts import render,redirect

# Create your views here.
#留言板函数
from board.models import Blogdesc
from login.models import Userinfo


def boardViews(request):
    if request.method == "GET":
        return render(request,'board.html')
    elif request.method == "POST":
        print(request.COOKIES)
        if 'uname' in request.COOKIES:
            title = request.POST['title']
            text = request.POST['desc']
            blog = Blogdesc()
            blog.title = title
            blog.desc = text
            blog.userid_id = Userinfo.objects.get(username=request.COOKIES['uname']).id
            blog.save()
            return redirect('/')
        else:
            return redirect('/login')
