from django.http import HttpResponse 
from django.shortcuts import render   #there is one method in django called redirect 
from .forms import UserForm            # this is used to call the forms page 

def homePage(request):
    data={
        'title':'Home Page',
        'bdata':'welcome to this new learning path',
        'numbers':[10,20,15,30,20]
    }
    return render(request,"index.html",data)

def submitform(request):                             #used for submit form must restart the server
    try:
        n1=request.GET['username']
        n2=request.GET['email']
        n3=request.GET['password']
        n4=request.GET['bio']
        print(n1+n2;)

        return redirect(url)
    except:
        pass

def aboutUS(request):
    if request.methods=="GET":
        output=request.GET.get('output')
    return render(request,"about-is.html",{'output':output})   

def services(request):
    return render(request,"services.html")

def marksheet(request):
    if request.method=="POST"
        s1=eval(request.POST.get('subject1'))
        s2=eval(request.POST.get('subject2'))
        s3=eval(request.POST.get('subject3'))
        t=s1+s2+s3
        p=t*100/3;
        if p>60:
            d="first dev"
        elif p>=48:
            d="second dev"
        elif p>=38:
            d="third dev"
        else:
            d="fail"
        data={
            'total'=t,
            'per'=p,
            'div'=d
        }
        return render(request,"marksheet.html",data)
    return render(request,"marksheet.html")

def saveoddoreven(request):
    c=''
    if request.method=="POST":
        #this is for the manual form 
        if request.POST.get('num1')=="":
            return render(request,"oddoreven.html",{'error':True})
            
        # this is for odd or even 
        n=eval(request.POST.get('num1'))
        if n%2==0:
            c="Even number"
        else:
            c="odd numbrt"
    return render(request,"oddoreven.html",{'c':10})

def calculator(request):
    try:
        c=''
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('num3')
            if opr=="+":
                c=n1+n2
            elif opr="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c==n1/n2    
    
    except:
        c="invalid operation"
    
    return render(request,"calculator.html",'{'c':c})

def coursedetails(request,course):
    return HttpResponse(course)

def userForm(request):
    finalans=0
    fn=UserForm()

    data={'form':fn}            # representation of use of dictionary 
    try:
        if request.method=="POST":
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            finalans=n1+n2
            data={
                'form':fn,
                'output':finalans
            }
            url="/about-us/?output={}".format(finalans)
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