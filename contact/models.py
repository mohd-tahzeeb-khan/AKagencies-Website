from django.db import models

# Create your models here.


class contactus(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=80)
    mobile=models.CharField(max_length=15)
    message=models.CharField(max_length=1000)
class contact_details(models.Model):
    Phone=models.CharField(max_length=11)
    Alternate_Phone_no=models.CharField(max_length=11)
    Instagram=models.URLField(max_length=250)
    Facebook=models.URLField(max_length=250)
    Twitter=models.URLField(max_length=250)
    Youtube=models.URLField(max_length=250)
    EmailId=models.EmailField(max_length=100)
    Location=models.CharField(max_length=1000, null=False, default="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d30711292.110871688!2d64.43748693609942!3d20.01115759964804!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x30635ff06b92b791%3A0xd78c4fa1854213a6!2sIndia!5e0!3m2!1sen!2sin!4v1666597009340!5m2!1sen!2sin")


