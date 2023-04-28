from django.contrib import admin
from contact_us.models import Contact
from django.template.defaultfilters import truncatechars
from django.utils.html import format_html
from django.urls import reverse
# Register your models here.
class Custom_contact(admin.ModelAdmin):
    list_display = ['main_heading','Title','Description','status_and_logo','Edit','Delete']
    ordering = ('id',)


    def Title(self,obj):
        return truncatechars(obj.title,40)
    Title.short_Title = 'Title'


    def has_add_permission(self, request):
        count = Contact.objects.count()
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
        return truncatechars(obj.description,40)
    Description.short_Description = "Description"


    
    

admin.site.register(Contact,Custom_contact)