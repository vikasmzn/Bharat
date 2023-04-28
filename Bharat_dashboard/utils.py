from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site


def send_email(request):
    if request.method == "POST":
            print(request.POST)
            name = request.POST.get('fullName')
            email = request.POST.get('emailId')
            designation = request.POST.get('designation')
            company_name = request.POST.get('compnayName')
            number = request.POST.get('phoneNumber')
            description = request.POST.get('description')

            
            from_email = settings.DEFAULT_FROM_EMAIL
            subject = "contact"
            to_email = email
            message = render_to_string('contact.html',{
                'name' : name,
                
                'designation' : designation,
                'description' : description,
                'company_name' : company_name,
                'number' : number,
                'email' : email



            })
            email =EmailMessage(subject,message,from_email,to=[to_email])
            email.send()