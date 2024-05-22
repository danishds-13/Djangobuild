"""
URL configuration for Djangproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Djangproject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-us/',views.aboutUS,name='about'),
    path('',views.homepage,name='home'),
    path('services/',views.services,name='services'),
    path('calculator/',views.calculator,name='calculator'),
    path('submitform/',views.submitform,name='submitform')
    path('coursedetails/<slug:course>',views.coursedetails),
    path('userform',views.userForm),
    path('saveoddoreven',views.saveoddoreven),
    path('marksheet',views.marksheet),
    path('newsDetails/<slug>',views.newsDetails),
    path('saveEnquiry/',views.saveEnquiry,name="saveEnquiry"),
]
