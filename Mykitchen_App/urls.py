from django.contrib import admin
from django.urls import path,include
from Mykitchen_App import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='About'),
    path('Services',views.Services,name='Services'),
    path('contact',views.contact,name='contact')
]
