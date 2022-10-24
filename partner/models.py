from django.db import models

# Create your models here.
class partners(models.Model):
    brand=models.CharField(max_length=25)