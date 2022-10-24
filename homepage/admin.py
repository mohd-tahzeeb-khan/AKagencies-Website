from django.contrib import admin
from homepage.models import homepage, navbar

class admin_homepage(admin.ModelAdmin):
    list=('heading', 'description_paragraph')
# Register your models here.
admin.site.register(homepage, admin_homepage)
class admin_navbar(admin.ModelAdmin):
    list=('navigations', 'navigationlinks')
admin.site.register(navbar, admin_navbar)