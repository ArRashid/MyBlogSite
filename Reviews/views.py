from django.shortcuts import render,HttpResponse

from .models import *

# Create your views here.

def Index(request):
    product = Product.objects.filter(pid=2).first()
    review =  Review.objects.filter(id=2).first()

    print(product.name)

    context = {
        'product': product,
        'review' : review
    }
    return render(request,"public/reviews/review.html",context)
