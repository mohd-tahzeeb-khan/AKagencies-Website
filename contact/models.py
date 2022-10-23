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


