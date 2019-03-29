#encoding:utf-8
from django.shortcuts import render

#主页函数
# Create your views here.
from board.models import Blogdesc


def indexViews(request):
    if 'uname' not in request.COOKIES:
        blogs = Blogdesc.objects.filter(userid__username='jiaopb').order_by('-date').all()
        if len(blogs) >= 4:
            blogs = blogs[:4]
        else:
            blogs = blogs
        print(list(blogs))
        print(locals())
        return render(request, 'index.html',{'blog':blogs})
    else:
        blogs = Blogdesc.objects.filter(userid__username=request.COOKIES['uname']).order_by('-date').all()
        if len(blogs) >= 4:
            blogs = blogs[:4]
        else:
            blogs = blogs
        print(list(blogs))
        return render(request, 'index.html', {'blog': blogs})










