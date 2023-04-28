from django.contrib import admin
from .models import Interviews,Education
from django.template.defaultfilters import truncatechars
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.
class Custom_interview(admin.ModelAdmin):
    list_display = ['Title','icon_title','Hyperlink','image','status_and_logo','Edit','Delete']
    ordering = ('id',)

    def Hyperlink(self,obj):
        return truncatechars(obj.hyperlink,50)
    Hyperlink.short_Hyperlink = "Hyperlink"


    def save_model(self, request, obj, form, change):
        model_id = obj.id
        obj.save()


    def Title(self,obj):
        return truncatechars(obj.title,40)
    Title.short_Title = "Title"

    
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

class Custom_Education(admin.ModelAdmin):
    list_display = ['Title','icon_title','Hyperlink','image_view','icon_view','status_and_logo','Edit','Delete']
    ordering =('id',)


    def Hyperlink(self,obj):
        return truncatechars(obj.hyperlink,50)
    Hyperlink.short_Hyperlink = "Hyperlink"

    def save_model(self, request, obj, form, change):
        model_id = obj.id
        obj.save()


    def Title(self,obj):
        return truncatechars(obj.title,40)
    Title.shor_Title = "Title"

    
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


admin.site.register(Education,Custom_Education)
admin.site.register(Interviews,Custom_interview)