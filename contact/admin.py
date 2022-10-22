from django.contrib import admin
from contact.models import contactus

# Register your models here.
class admin_contactus(admin.ModelAdmin):
    list=('name', 'email', 'mobile', 'message')
admin.site.register(contactus, admin_contactus)