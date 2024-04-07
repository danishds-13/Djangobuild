from django.http import HttpResponse 
from django.shortcuts import render   #there is one method in django called redirect 

def homePage(request):
    data={
        'title':'Home Page',
        'bdata':'welcome to this new learning path',
        'numbers':[10,20,15,30,20]
    }
    return render(request,"index.html",data)

def aboutUS(request):
    if request.methods=="GET":
        output=request.GET.get('output')
    return render(request,"about-is.html",{'output':output})   

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

# use of post command :-
#def userForm(request):
#    finalans=0
#    try:
#       if request.method=="POST"
#        n1=request.POST['username']
#        n2=request.POST['email']
#        n3=request.POST['password']
#        n4=request.POST['bio']
#       finalans=n1+n2
#        data={
#                'n1':n1,
#                'n2':n2,
#                'output':finalans
#       }
#        url="/about-us/?output={}".format{finalans}   #same in line - 13,14,15
#        
#        return HttpResponseRedirect(url)
#    except:
#        pass
#    return render("userform.html",data)