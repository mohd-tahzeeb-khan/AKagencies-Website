from django.db import models

# Create your models here
class project(models.Model):
    image=models.ImageField(upload_to='projects/')
    companyname=models.CharField(max_length=150)
    categoryproject=models.CharField(max_length=25)