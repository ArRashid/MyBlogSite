from email.mime import image
from django.db import models
from taggit.managers import TaggableManager
# Create your models here.


class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to="uploads/blog/posts",blank=True,null=True)
    author = models.CharField(max_length=100)
    date = models.DateField()
    tages = TaggableManager()
    category = models.CharField(max_length=25)
    content = models.TextField()

    def __str__(self):
        return self.title


