from django.db import models

# Create your models here
class project(models.Model):
    image=models.ImageField()
    companyname=models.CharField(max_length=20)
    categoryproject=models.CharField(max_length=15)