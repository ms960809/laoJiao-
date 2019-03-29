from django.conf.urls import url
from .views import *

# Create your views here.
urlpatterns = [

    url(r'^$',articleViews,name='article'),
    url(r'^desc/\d*$',descViews,name='desc'),

]