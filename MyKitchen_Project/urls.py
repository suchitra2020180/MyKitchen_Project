"""MyKitchen_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

#added admin from google  ##Django admin text
admin.site.site_header = "My_Kitchen Admin"
admin.site.site_title = "My_Kitchen Admin Portal"
admin.site.index_title = "Welcome to My_Kitchen Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Mykitchen_App.urls')),
    path('index',include('Mykitchen_App.urls')),
    path('sendvariabletoTemplate',include('Mykitchen_App.urls')),
    path('My_Kitchen_page',include('Mykitchen_App.urls')),
    path('about',include('Mykitchen_App.urls')),
    path('Services',include('Mykitchen_App.urls')),
    path('contact',include('Mykitchen_App.urls'))
]
