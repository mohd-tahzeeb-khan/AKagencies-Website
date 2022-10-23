from django.contrib import admin

# Register your models here.
from service.models import services
class admin_service(admin.ModelAdmin):
    list=('Service_provided','Service_description','Service_image')
admin.site.register(services, admin_service)