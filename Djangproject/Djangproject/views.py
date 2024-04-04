from django.http import HttpResponse 
from django.shortcuts import render

def homePage(request):
    data={
        'title':'Home Page',
        'bdata':'welcome to this new learning path',
        'numbers':[10,20,15,30,20]
    }
    return render(request,"index.html",data)

def aboutUS(request):
    return HttpResponse("welcome to Example page")

def services(request):
    return render(request,"services.html")

def coursedetails(request,course):
    return HttpResponse(course)

def userForm(request):
    finalans=0
    try:
        n1=request.GET['username']
        n2=request.GET['email']
        n3=request.GET['password']
        n4=request.GET['bio']
        print(n1+n2;)
    except:
        pass
    return render("userform.html",{'output':finalans})