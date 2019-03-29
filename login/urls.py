from django.conf.urls import url
from .views import *

# Create your views here.
urlpatterns = [
    url(r'^$',loginViews,name='log'),
    url(r'^ajax/$',ajaxViews,name='ajax'),
    url(r'^logout',logoutViews,name='logout'),
]