from django.db import models

# Create your models here.


class homepage(models.Model):
    heading=models.CharField(max_length=50)
    description_paragraph=models.CharField(max_length=200)
class navbar(models.Model):
    navigations=models.CharField(max_length=12,default="Home")
    navigantionlinks=models.CharField(max_length=25, default="#")
