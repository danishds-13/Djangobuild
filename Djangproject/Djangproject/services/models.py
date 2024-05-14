from django.contrib import admin 
from autoslug import AutoSlugField   #slugfield

class Service(models.Model):
    service_icon=models.CharField(max_length=50)
    service_title=models.models.CharField(max_length=50)
    service_des=models.TextField()                                    #python manage.py makemigrations  And should be able to see the services in the db as well 

#Register your models here   

# this is for the tinymce
from django.db import models 
from tinymce.models import HTMLField
class News(models.Model):
    news_title=models.models.CharField(max_length=50)
    news_desc=HTMLField()

#slug = autoslug field (EG: ABOUT US page to about-us without the id)
news_slug=AutoSlugField(populate_from='title',unique=True,null=True,default=None)