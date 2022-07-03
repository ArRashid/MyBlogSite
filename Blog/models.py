from math import fabs
from django.db import models
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField


from users.models import *
# Create your models here.


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=25)

    def __str__(self):
        return self.category

class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to="uploads/blog/posts",blank=True,null=True)
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    date = models.DateField()
    mdate = models.DateField(null=True,blank=True)
    tags = TaggableManager(blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    content = RichTextUploadingField()
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    postid = models.ForeignKey(Posts,on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=100)
    email = models.EmailField(default='no@email.exist')
    comment = models.TextField()
    is_author = models.BooleanField(default=False)
    



