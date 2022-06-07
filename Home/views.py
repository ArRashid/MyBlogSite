from django.shortcuts import render,HttpResponse

from Home.models import Features

# Create your views here.

def Index(request):
    features = Features.objects.all()

    context={
    'features':features
    }
    return render(request,"home-index.html",context)

def Blog(request):
    return render(request,"home-blog.html")


def Post(request):
    return render(request,"home-blog-post.html")


def Study(request):
    return render(request,"home-study.html")

def Comunity(request):
    return render(request,"home-comunity.html")

def Media(request):
    return render(request,"home-media.html")
def Team(request):
    return render(request,"home-team.html")
def Port(request):
    return render(request,"home-port.html")
def Services(request):
    return render(request,"home-services.html")



