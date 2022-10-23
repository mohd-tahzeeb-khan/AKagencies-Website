from django.db import models

# Create your models here.
class testimonials(models.Model):
    name=models.CharField(max_length=15)
    profession=models.CharField(max_length=15)
    image=models.ImageField()
    message=models.CharField(max_length=150)