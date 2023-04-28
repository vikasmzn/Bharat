from django.urls import path
from .import views


urlpatterns = [
    path('',views.homepage,name='home'),
    path('knowl/',views.knowledge,name='knowl'),
    path('about_us/',views.about_us,name='about_us'),
    path('contact_us/',views.Contact_us,name='contact_us'),
    path('press-release/',views.press_release,name='press-release'),
    path('send_mail',views.send_mail,name='send_mail'),
]
