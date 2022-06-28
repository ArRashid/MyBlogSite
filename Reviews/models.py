

from django.db import models


from users.models import CustomUser
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category =  models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Product(models.Model):
    pid = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    cover = models.ImageField(upload_to="uploads/reviews/product",blank=True,null=True)
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    price = models.IntegerField()
    def __str__(self):
        return self.name



class Review(models.Model):
    id = models.AutoField(primary_key=True)
    pid = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    date = models.DateField()
    spec = RichTextUploadingField()
    pros = models.TextField()
    cons = models.TextField()
    vform = models.IntegerField(null=True,blank=True)
    bqulity = models.IntegerField(null=True,blank=True)


    def create_link(*kwargs):
        l = Link(kwargs=kwargs)
        l.save()
    def create_product(*kwargs):
        p = Product(kwargs=kwargs)
        p.save()
    def create_category(*kwargs):
        c = Category(kwargs=kwargs)
        c.save()

    def __str__(self):
        return self.title
    

    
class Link(models.Model):
    id = models.AutoField(primary_key=True)
    review_id = models.ForeignKey(Review,on_delete=models.CASCADE)
    site = models.CharField(max_length=200)
    icon = models.ImageField(upload_to="uploads/reviews/link",blank=True,null=True)
    link =  models.CharField(max_length=200)





