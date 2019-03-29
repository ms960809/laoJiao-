from django.conf.urls import url
from .views import *

# Create your views here.
urlpatterns = [
    url(r'^$',aboutViews,name='about'),

]