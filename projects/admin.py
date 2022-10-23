from django.contrib import admin
from projects.models import project
# Register your models here.
class admin_project(admin.ModelAdmin):
    list=('Image', 'companyname','categoryproject')
admin.site.register(project, admin_project)