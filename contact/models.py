from django.db import models

# Create your models here.


class contactus(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=80)
    mobile=models.CharField(max_length=15)
    message=models.CharField(max_length=1000)
