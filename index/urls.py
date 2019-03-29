from django.conf.urls import url
from .views import *

# Create your views here.
urlpatterns = [
    url(r'^$',indexViews,name='index'),
]