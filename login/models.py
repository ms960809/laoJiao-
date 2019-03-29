import django.utils.timezone as timezone
from django.db import models
# Create your models here.

#用户信息表
class Userinfo(models.Model):
    class Meta:
        db_table = 'userinfo'
        verbose_name = '用户信息表'
        verbose_name_plural = '用户信息表'


    userimage = models.ImageField(upload_to='user/head_image/',null=True,verbose_name='用户头像')
    username = models.CharField(max_length=200,null=False,verbose_name='用户名')
    password = models.CharField(max_length=200,null=False,verbose_name='用户密码')
    phone = models.CharField(max_length=200,null= False,verbose_name='手机号码')
    cdate = models.DateTimeField(default=timezone.now,null=False,verbose_name='注册时间')
    isActive = models.BooleanField(default=True,null=False,verbose_name='活跃')

    def __str__(self):
        return self.username