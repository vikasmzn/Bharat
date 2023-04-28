from django.contrib import admin
from Header.models import *
from django.utils.html import format_html
from django.urls import reverse
# Register your models here.
class Custom_Header(admin.ModelAdmin):
    list_display = ['menu','hyperlink','status_and_logo',"Edit",'Delete']
    ordering = ('id',)

    def save_model(self, request, obj, form, change):
        model_id = obj.id
        obj.save()
    
    
    def Edit(self, obj):
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
    
        return format_html('<a href="{}" style = "font-weight : 600">Edit</a>', url)
        
    Edit.short_description = 'Edit'
    Edit.allow_tags = True


    def Delete(self, obj):
        url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html('<a href="{}" style="color:red; font-weight:bold">Delete</a>', url)
    Delete.short_description = 'Delete'
    Delete.allow_tags = True

class custom_logo(admin.ModelAdmin):
    list_display = ['image','hyperlink','status_and_logo','Edit','Delete']
    ordering = ('id',)


    def has_add_permission(self, request):
        count = Header_logo.objects.count()
        if count > 0:
            return False
        return True

    def save_model(self, request, obj, form, change):
        model_id = obj.id
        obj.save()
    
    def Edit(self, obj):
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
    
        return format_html('<a href="{}" style = "font-weight : 600">Edit</a>', url)
        
    Edit.short_description = 'Edit'
    Edit.allow_tags = True


    def Delete(self, obj):
        url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html('<a href="{}" style="color:red; font-weight:bold">Delete</a>', url)
    Delete.short_description = 'Delete'
    Delete.allow_tags = True

admin.site.register(Header_menu,Custom_Header)
admin.site.register(Header_logo,custom_logo)
