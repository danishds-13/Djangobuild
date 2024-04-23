from django.contrib import admin 
class Service(models.Model):
    service_icon=models.CharField(max_length=50)
    service_title=models.models.CharField(max_length=50)
    service_des=models.TextField()                                    #python manage.py makemigrations  And should be able to see the services in the db as well 

#Register your models here   