from django.db import models
from login.models import Userinfo
import django.utils.timezone as timezone

# Create your models here.

# 博客信息表
class Blogdesc(models.Model):


    class Meta:
        db_table = 'blogdesc'
        verbose_name = '博客信息表'
        verbose_name_plural = '博客信息表'
    title = models.CharField(max_length=500,null=False,verbose_name='博客标题')
    desc = models.CharField(max_length=1024*10,null=False,verbose_name='博客内容')
    date = models.DateTimeField(default=timezone.now,null=False,verbose_name='创作时间')
    userid = models.ForeignKey(Userinfo,verbose_name='作者')
    isActive = models.BooleanField(default=True,null=False,verbose_name='活跃')