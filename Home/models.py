from distutils.command.upload import upload
from statistics import mode
import traceback
from django.db import models

# Create your models here.


class Features(models.Model):
    title = models.CharField(max_length=25)
    details = models.CharField(max_length=100)
    link = models.CharField(max_length=100,default="www.google.com")
    icon = models.ImageField(upload_to="uploads/icons/features",blank=True,null=True)

    def __str__(self):
        return self.title


class AppsMenu(models.Model):
    title = models.CharField(max_length=10)
    link = models.CharField(max_length=100)
    is_active = models.BooleanField()
    def __str__(self):
        return self.title


class ContactMe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=150,null=True,blank=True)
    email = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.email


class MyCertificate(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="uploads/home/myself/certificate",blank=True,null=True)
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=500,null=True,blank=True)
    @property
    def get_detail(self):
        if self.detail:
              return self.detail
        else:
              return ""