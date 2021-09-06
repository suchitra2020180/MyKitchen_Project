from django.shortcuts import render,HttpResponse
from datetime import datetime
from Mykitchen_App.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'index.html')

def SendVariableToTemplate(request):
    context= {
        'variable1':'Give your variable here',
        'variable2':'VARIABLE IS BOLDED HERE'

    }
    return render(request,'SendVariableToTemplate.html',context)

def My_Kitchen_page(request):
    return render(request,'My_Kitchen_page.html')
    
def home(request):
    return HttpResponse('This is home page')

def about(request):
    return render(request,'About.html')

def Services(request):
    return render(request,'Services.html')

def contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        desc = request.POST.get('desc')
        contact=Contact(name=name,email=email, mobile=mobile,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Message sent successully!') 

    return render(request,'Contact.html')

def address(request):
    return HttpResponse('This is Contact page')     
    