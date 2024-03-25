from django.http import HttpResponse 

def aboutUS(request):
    return HttpResponse("welcome to Example page")

def coursedetails(request,course):
    return HttpResponse(course)