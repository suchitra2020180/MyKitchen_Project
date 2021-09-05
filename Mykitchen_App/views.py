from django.shortcuts import render,HttpResponse

# Create your views here.
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
    