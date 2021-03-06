# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-26 11:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userimage', models.ImageField(null=True, upload_to='user/head_image/', verbose_name='用户头像')),
                ('username', models.CharField(max_length=200, verbose_name='用户名')),
                ('password', models.CharField(max_length=200, verbose_name='用户密码')),
                ('phone', models.CharField(max_length=200, verbose_name='手机号码')),
                ('cdate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='注册时间')),
                ('isActive', models.BooleanField(default=True, verbose_name='活跃')),
            ],
            options={
                'verbose_name': '用户信息表',
                'verbose_name_plural': '用户信息表',
                'db_table': 'userinfo',
            },
        ),
    ]
