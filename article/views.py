from django.shortcuts import render

# Create your views here.
#博客文章函数
from board.models import Blogdesc


def articleViews(request):
    if 'uname' not in request.COOKIES:
        blogs = Blogdesc.objects.filter(userid__username='jiaopb').order_by('-date').all()
        if len(blogs) >= 4:
            blogs = blogs[:4]
        else:
            blogs = blogs
        print(list(blogs))
        print(locals())
        return render(request, 'article.html',{'blog':blogs})
    else:
        blogs = Blogdesc.objects.filter(userid__username=request.COOKIES['uname']).order_by('-date').all()
        if len(blogs) >= 4:
            blogs = blogs[:4]
        else:
            blogs = blogs
        print(list(blogs))
        return render(request, 'article.html', {'blog': blogs})

def descViews(request):
    if 'uname' in request.COOKIES:
        print('--------')
        blog = Blogdesc.objects.get(userid__username=request.COOKIES['uname'],id = request.GET['id'])
        print(blog)
        print(type(blog))
        return render(request,'desc.html',{'bg':blog})
    else:
        blog = Blogdesc.objects.get(userid__username='jiaopb',id = request.GET['id'])
        return render(request,'desc.html',{'bg':blog})
