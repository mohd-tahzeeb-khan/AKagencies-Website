from django.contrib import admin
from testimonials.models import testimonials
# Register your models here.
class admin_testimonials(admin.ModelAdmin):
    list=('name', 'profession', 'image', 'message')
admin.site.register(testimonials, admin_testimonials)