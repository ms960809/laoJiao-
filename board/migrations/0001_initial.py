# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-26 11:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogdesc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='博客标题')),
                ('desc', models.CharField(max_length=10240, verbose_name='博客内容')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创作时间')),
                ('isActive', models.BooleanField(default=True, verbose_name='活跃')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Userinfo', verbose_name='创作人id')),
            ],
            options={
                'verbose_name': '博客信息表',
                'verbose_name_plural': '博客信息表',
                'db_table': 'blogdesc',
            },
        ),
    ]
