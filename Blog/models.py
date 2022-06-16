from django.db import models
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
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
    author = models.CharField(max_length=100)
    date = models.DateField()
    tages = TaggableManager()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    postid = models.ForeignKey(Posts,on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=100)
    email = models.EmailField(default='no@email.exist')
    comment = models.TextField()
    



