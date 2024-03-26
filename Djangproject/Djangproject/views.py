from django.http import HttpResponse 
from django.shortcuts import render

def homePage(request):
    return render(request,"index.html")

def aboutUS(request):
    return HttpResponse("welcome to Example page")

def coursedetails(request,course):
    return HttpResponse(course)