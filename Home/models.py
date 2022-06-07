from distutils.command.upload import upload
from statistics import mode
import traceback
from django.db import models

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=20)
    imga = models.ImageField(upload_to="images/")

class Features(models.Model):
    title = models.CharField(max_length=25)
    details = models.CharField(max_length=100)
    link = models.CharField(max_length=100,default="www.google.com")
    icon = models.ImageField(upload_to="uploads/icons/features",blank=True,null=True)