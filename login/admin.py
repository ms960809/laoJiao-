from django.contrib import admin

# Register your models here.
from login.models import Userinfo


class UserinfoAdmin(admin.ModelAdmin):
    list_display = ['username','phone','cdate','isActive']
    list_display_links = ['username']
    search_fields = ['username','phone','cdate']
    list_filter = ['username','phone','cdate']
    date_hierarchy = 'cdate'
    fieldsets = (
        ('基本选项',{
            'fields':('username','userimage','phone','isActive'),
        }),
         ('高级选项',{
             'fields':('password',),
             'classes':('collapse',)
         })
    )


admin.site.register(Userinfo,UserinfoAdmin)