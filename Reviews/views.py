from django.shortcuts import render,HttpResponse

from .models import *

# Create your views here.

def Index(request):
    
    review =  Review.objects.filter(id=1).first()
    vk = review.get_all()
    for i  in vk["analogy"]: 
        print(i.title)
    return render(request,"public/reviews/review.html",context=vk)
