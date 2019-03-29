from django.shortcuts import render

# Create your views here.

def aboutViews(request):
    return render(request,'about.html')