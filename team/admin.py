from django.contrib import admin
from team.models import team
# Register your models here.
class admin_team(admin.ModelAdmin):
    list=('Name', 'desgination', 'image')
admin.site.register(team, admin_team)