from django.contrib import admin
from .models import About,what_we_do
from django.template.defaultfilters import truncatechars
from django.urls import reverse
from django.utils.html import format_html

# Register your models here.
class custom_about(admin.ModelAdmin):

    list_display = ['title','Description','image_title','image_view','status_and_logo','Edit','Delete']
    ordering = ('id',)

    def has_add_permission(self, request):
        count = About.objects.count()
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


    def Description(self,obj):
        return truncatechars(obj.description,50)
    Description.short_Description = "Description"


class custom_what_we_do(admin.ModelAdmin):
    list_display = ['title','Description','image_view','status_and_logo','Edit','Delete']
    ordering = ('id',)

    
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



    def Description(self,obj):
        return truncatechars(obj.description,50)
    Description.short_Description = "Description"


    def save_model(self, request, obj, form, change):
        model_id = obj.id
        obj.save()


admin.site.register(About,custom_about)
admin.site.register(what_we_do,custom_what_we_do)