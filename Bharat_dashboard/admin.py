from django.contrib import admin
from .models import BannerImage,Our_vision,Our_focus,Our_members,Media_center,Press_Image,Press_release
from django.template.defaultfilters import truncatechars
from django.urls import reverse
from django.utils.html import format_html

class Bharat_dashboard(admin.AdminSite):
    verbose_name_plural = "New App Name"

admin.site.__class__ = Bharat_dashboard



# Register your models here.
class Custom_banner(admin.ModelAdmin):
    list_display = ['title','button','hyperlink','image','status_and_logo','Edit','Delete']

    def has_add_permission(self, request):
        count = BannerImage.objects.count()
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

class Custom_Vision(admin.ModelAdmin):
    list_display = ['main_heading','title','description','button','hyperlink','image_show','status_and_logo','Edit','Delete']
    ordering = ('id',)

#for edit button
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


    def save_model(self, request, obj, form, change):
        model_id = obj.id
        obj.save()



class Custom_focus(admin.ModelAdmin):
    list_display = ['title','description','image_show','status_and_logo','Edit','Delete']
    ordering = ('id',)

    def save_model(self, request, obj, form, change):
        model_id = obj.id
        obj.save()


# for edit button
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

class Custom_members(admin.ModelAdmin):
    list_display = ['image_show','status_and_logo','Edit','Delete']
    ordering = ('id',)

#for edit button
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

    def save_model(self, request, obj, form, change):
        model_id = obj.id
        obj.save()

class Custom_media(admin.ModelAdmin):
    list_display = ['title','hyperlink','image_show','status_and_logo','Edit','Delete']
    ordering = ('id',)

    def save_model(self, request, obj, form, change):
        model_id = obj.id
        obj.save()

#for edit button
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

class custom_press_image (admin.ModelAdmin):
    list_display = ['image_view','status_and_logo','Edit','Delete']
    ordering = ('id',)


#for edit button
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


    def save_model(self, request, obj, form, change):
        model_id = obj.id
        obj.save()

class custom_press_release (admin.ModelAdmin):
    list_display = ['image_view','Title','Hyperlink','status_and_logo','Edit','Delete']
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


    def save_model(self, request, obj, form, change):
        model_id = obj.id
        obj.save()


# for truncate the title 
    def Title(self,obj):
        return truncatechars(obj.title,40)
    Title.short_Title = "Title"


#for truncate the description
    def Hyperlink(self,obj):
        return truncatechars(obj.hyperlink,50)
    Hyperlink.short_Hyperlink = "Hyperlink"

admin.site.register(BannerImage,Custom_banner)
admin.site.register(Our_vision,Custom_Vision)
admin.site.register(Our_focus,Custom_focus)
admin.site.register(Our_members,Custom_members)
admin.site.register(Media_center,Custom_media)
admin.site.register(Press_Image,custom_press_image)
admin.site.register(Press_release,custom_press_release)