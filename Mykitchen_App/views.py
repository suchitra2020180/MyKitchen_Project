from django.shortcuts import render,HttpResponse

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
    return render(request,'Contact.html')

def address(request):
    return HttpResponse('This is Contact page')     
    