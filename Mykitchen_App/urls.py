from django.contrib import admin
from django.urls import path,include
from Mykitchen_App import views

urlpatterns = [
    path('',views.home,name='home'),
    path('index',views.index,name='index'),
    path('sendvariabletoTemplate',views.SendVariableToTemplate,name='sendvariabletoTemplate'),
    path('My_Kitchen_page',views.My_Kitchen_page,name='My_Kitchen_page'),
    path('about',views.about,name='About'),
    path('Services',views.Services,name='Services'),
    path('contact',views.contact,name='contact')
]
