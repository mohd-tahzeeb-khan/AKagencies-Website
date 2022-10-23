from django.db import models

# Create your models here.
class team(models.Model):
    Name=models.CharField(max_length=40)
    designation=models.CharField(max_length=30)
    image=models.ImageField(upload_to='team/')