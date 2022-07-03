from django.contrib import admin

from .models import Category,Product,Review,Link,Rating,Analogy,Comment
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Link)
admin.site.register(Rating)
admin.site.register(Analogy)
admin.site.register(Comment)

