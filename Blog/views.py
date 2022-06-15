
from unicodedata import category
from django.shortcuts import render ,HttpResponse
from django.utils.translation import gettext_lazy as _

from Blog.models import *



# main Variables 
allcat = Category.objects.all()


# Main Mathods
def get_allposts(show=5,page=1):
    posts = Posts.objects.all().order_by('-date')             # Blog object quarry
    pno =range(int(posts.count()/show)+1)   # range of pages 
    index = (page -1) * show #shat showin post from here 
    context = {
            'posts' : posts[index:index + show],
            'pages' : pno,
            'index' : page - 1,
            'category': allcat   
        }
    return context

def get_catposts(category,show=5,page=1):
    cat  = Category.objects.filter(category=category).values('id')    
    posts = Posts.objects.all().filter(category=cat[0]['id']).order_by('-date')      # Blog object quarry
    pno =range(int(posts.count()/show))   # range of pages 
    index = (page -1) * show #shat showin post from here 
    context = {
            'posts' : posts[index:index + show],
            'pages' : pno,
            'index' : page - 1,
            'current_category':category
        }
    return context





# Create your views here.
def Index(request):
    if request.user.is_authenticated:
        return HttpResponse("Welcome to special Blog")
    else:  
        

        return render(request,"public/blog/blog-index.html",context=get_allposts())

def Pages(request,pageno):
    if request.user.is_authenticated:
        return HttpResponse("Welcome to special Blog")

    else:
        return render(request,"public/blog/blog-index.html",context=get_allposts(page=pageno))



def Category_Post(request,category,pageno=1):
     if request.user.is_authenticated:
        return HttpResponse("Welcome to special Blog")

     else:
        
        return render(request,"public/blog/blog-index.html",context=get_catposts(category,page=pageno))

