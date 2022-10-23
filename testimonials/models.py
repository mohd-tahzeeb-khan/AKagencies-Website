from django.db import models

# Create your models here.
class testimonials(models.Model):
    name=models.CharField(max_length=50)
    profession=models.CharField(max_length=40)
    image=models.ImageField(upload_to='testimonials/')
    message=models.CharField(max_length=250)