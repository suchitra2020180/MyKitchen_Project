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
    
def home(request):
    return HttpResponse('This is home page')

def about(request):
    return HttpResponse('This is about page')

def Services(request):
    return HttpResponse('This is Services page')

def contact(request):
    return HttpResponse('This is Contact page')   

def address(request):
    return HttpResponse('This is Contact page')     
    