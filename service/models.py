from django.db import models

# Create your models here.
class services(models.Model):
    Service_image=models.ImageField(upload_to='services/')
    Service_provided=models.CharField(max_length=20)
    Service_description=models.CharField(max_length=100)