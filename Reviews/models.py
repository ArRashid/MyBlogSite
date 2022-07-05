

from itertools import product
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
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    cover = models.ImageField(upload_to="uploads/reviews/products",blank=True,null=True)
    brand = models.CharField(max_length=200)
    price = models.IntegerField()
    def __str__(self):
        return self.name



class Review(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    date = models.DateField()
    spec = RichTextUploadingField()
    pros = models.TextField()
    cons = models.TextField()
    

        
    def create_category(self,category):
        c = Category(category=category)
        c.save()
    def get_product(self):
        return Product.objects.filter(id=self.product_id).first()
    def get_rating(self):
        return Rating.objects.filter(product=self.product).all()
    def get_link(self):
        return Link.objects.filter(review=self).all()
    def get_analogy(self):
        return Analogy.objects.filter(product=self.product).all()
    def get_comment(self):
        return Comment.objects.filter(review=self).all()
    def get_all(self):
        var = {
            'product': self.get_product(),
            'rating': self.get_rating(),
            'analogy': self.get_analogy(),
            'link' : self.get_link(),
            'review' : self,
            'comments':self.get_comment,
            'activeapp':'REVIEWS'
        }
        return var
   
    


    def __str__(self):
        return self.title
    
class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    max_rate= models.IntegerField()
    rate= models.IntegerField()
    site = models.CharField(max_length=25)

class Analogy(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    percent = models.IntegerField()
    

class Link(models.Model):
    id = models.AutoField(primary_key=True)
    review = models.ForeignKey(Review,on_delete=models.CASCADE)
    site = models.CharField(max_length=200)
    icon = models.ImageField(upload_to="uploads/reviews/link",blank=True,null=True)
    link =  models.CharField(max_length=200)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    review = models.ForeignKey(Review,on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=100)
    email = models.EmailField(default='no@email.exist')
    comment = models.TextField()
    is_author = models.BooleanField(default=False)







