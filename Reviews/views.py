from django.shortcuts import render,HttpResponse

# Create your views here.

def Index(request):
    return render(request,"public/reviews/review.html")
