from django.contrib import admin
from partner.models import partners
# Register your models here.
class admin_partner(admin.ModelAdmin):
    list=('brand')
admin.site.register(partners,admin_partner)