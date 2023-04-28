
from django.shortcuts import render,redirect
from Bharat_dashboard.models import *
from knowledge_center.models import *
from about_us.models import *
from Header.models import *
from django import forms
from contact_us.models import Contact
from contact_us.forms import contact_form
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages

# Create your views here.

def homepage(request):
    header_menu = Header_menu.objects.filter(status = 1).order_by('id')
    header_logo = Header_logo.objects.filter(status = 1).order_by('id')
    banner_image = BannerImage.objects.filter(status = 1).order_by('id')
    our_vision = Our_vision.objects.filter(status = 1).order_by('id')
    our_focus = Our_focus.objects.filter(status = 1).order_by('id')
    our_members = Our_members.objects.filter(status = 1).order_by('id')
    media_center = Media_center.objects.filter(status = 1).order_by('id')
    context = {
        'header_menu' : header_menu,
        'header_logo' : header_logo,
        'banner_image' : banner_image,
        'our_vision' : our_vision,
        'our_focus' : our_focus,
        'our_members' : our_members,
        'media_center' : media_center,
    }
    return render(request,'index.html',context)


def knowledge(request):
    header_menu = Header_menu.objects.filter(status = 1).order_by('id')
    header_logo = Header_logo.objects.filter(status = 1).order_by('id')
    interview = Interviews.objects.filter(status = 1).order_by('id')
    education = Education.objects.filter(status = 1).order_by('id')
    context = {
        'header_menu' : header_menu,
        'header_logo' : header_logo,
        'interview' : interview,
        'education' : education,
    }
    return render(request,'Knowl.html',context)


def about_us(request):
    header_menu = Header_menu.objects.filter(status = 1).order_by('id')
    header_logo = Header_logo.objects.filter(status = 1).order_by('id')
    about = About.objects.filter(status = 1).order_by('id')
    What_we_do = what_we_do.objects.filter(status = 1).order_by('id')
    context = {
        'header_menu' : header_menu,
        'header_logo' : header_logo,
        'about' : about,
        'What_we_do' : What_we_do,
    }
    return render(request,'AboutUs.html',context)

def Contact_us(request):

    header_menu = Header_menu.objects.filter(status = 1).order_by('id')
    header_logo = Header_logo.objects.filter(status = 1).order_by('id')
    contact = Contact.objects.filter(status = 1).order_by('id')
    context = {
        'header_menu' : header_menu,
        'header_logo' : header_logo,
        'contact' : contact,
    }
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('fullName')
        email = request.POST.get('emailId')
        designation = request.POST.get('designation')
        company_name = request.POST.get('compnayName')
        number = request.POST.get('phoneNumber')
        description = request.POST.get('description')

        # if not all([name, email, number,company_name,description]):
        #     messages.error(request, "All fields are required.")
            

        domain = get_current_site(request)
        from_email = settings.DEFAULT_FROM_EMAIL
        subject = "contact"
        to_email = settings.CUSTOM_EMAIL
        message = render_to_string('contact.html',{
            'name' : name,
            'domain' : domain,
            'designation' : designation,
            'description' : description,
            'company_name' : company_name,
            'number' : number,
            'email' : email



        })
        email =EmailMessage(subject,message,from_email,to=[to_email])
        email.send()
        if email.send():
            messages.success(request,'Thank you for contacting us')
        else:
            messages.error(request,"Error in submitting your mail")
        
        return redirect('contact_us')
        

    return render(request,'contact_us.html',context)

def press_release(request):
    header_menu = Header_menu.objects.filter(status = 1).order_by('id')
    header_logo = Header_logo.objects.filter(status = 1).order_by('id')
    press_image = Press_Image.objects.filter(status = 1).order_by('id')
    release = Press_release.objects.filter(status = 1).order_by('id')
    our_members = Our_members.objects.filter(status = 1).order_by('id')
    
    context = {
        'header_menu' : header_menu,
        'header_logo' : header_logo,
        'press_image' : press_image,
        'release' : release,
        'our_members' : our_members,
    }
    return render(request,'Press-Release.html',context)

def our_vision(request):
    
    return render(request,'Vision.html')




def send_mail(request):
    if request.method == "POST":
        print(request.POST)
        user_name = request.POST['USerFullName']
        user_email  = request.POST['UserEmail']
        user_designation = request.POST['UserDesignation']
        from_email = settings.DEFAULT_FROM_EMAIL
        subject = 'Contact'

        to_email = user_email
        message = render_to_string('footer_mail.html',{
            'user_name' : user_name,
            'user_email' : user_email,
            'user_designation' : user_designation
        })
        email_send = EmailMessage(subject,message,from_email,to=[to_email])
        email_send.send()
        return redirect('home')

    return render(request, 'includes/footer.html')


