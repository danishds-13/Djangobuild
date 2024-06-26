from django.contrib import admin 
from service.models import Service
class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_icon','service_title','service_des')    #give permissions 

admin.site.register(Service,ServiceAdmin)
#Register your models here 

# for tinymce (settings>models>settings>admins)
from news.model import News 

class NewsAdmin(admin.ModelAdmin):
    list_display=('news_title','news_desc')

admin.site.register(News,NewsAdmin)