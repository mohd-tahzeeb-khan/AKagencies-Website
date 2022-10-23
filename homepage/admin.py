from django.contrib import admin
from homepage.models import homepage

class admin_homepage(admin.ModelAdmin):
    list=('heading', 'description_paragraph')
# Register your models here.
admin.site.register(homepage, admin_homepage)