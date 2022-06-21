from email.mime import image
from django.db import models

# Create your models here.
class ImgModel(models.Model):
    caption=models.CharField(max_length=200)
    image=models.ImageField()
    
    