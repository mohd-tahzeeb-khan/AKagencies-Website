from django.db import models

# Create your models here.


class homepage(models.Model):
    heading=models.CharField(max_length=50)
    description_paragraph=models.CharField(max_length=200)
