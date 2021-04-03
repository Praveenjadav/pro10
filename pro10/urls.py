"""pro10 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from app10 import views
views_app10=views
from app20 import views
views_app20=views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views_app10.index,name="index"),
    path('sample10/',views_app10.sample10,name="sample10"),
    path('index20/', views_app20.index,name="index20"),
    path('sample20/',views_app20.sample20,name="sample20"),
    
]
