from django.contrib import admin
from .models import *
# Register your models here.

#留言
class BlogdescAdmin(admin.ModelAdmin):
    list_display = ['title','date','userid','isActive']
    list_display_links = ['title']
    list_editable = ['isActive']
    search_fields = ['title','isActive']
    list_filter = ['date']
    date_hierarchy = 'date'

    fieldsets = (
        ('基本选项', {
            'fields': ('title', 'desc','userid'),
        }),
        ('高级选项', {
            'fields': ('date','isActive'),
            'classes': ('collapse',)
        })
    )

# admin.site.register(Blogdesc)
admin.site.register(Blogdesc,BlogdescAdmin)