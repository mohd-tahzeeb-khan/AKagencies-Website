from django.contrib import admin
from contact.models import contactus, contact_details

# Register your models here.
class admin_contactus(admin.ModelAdmin):
    list=('name', 'email', 'mobile', 'message')
admin.site.register(contactus, admin_contactus)
class admin_contactusdetails(admin.ModelAdmin):
    list=('Phone', 'Alternate_Phone_no', 'Instagram', 'Facebook', 'Twitter', 'Youtube', 'EmailId')
admin.site.register(contact_details, admin_contactusdetails)