from curses.ascii import HT
from unicodedata import category
from django.shortcuts import render,HttpResponse,redirect

from .models import *



# Main Mathods
def get_allposts(show=5,page=1):
    reviews = Review.objects.all().order_by('-date')             # Blog object quarry
    pno =range(int(reviews.count()/show)+1)   # range of pages 
    index = (page -1) * show #shat showin post from here 
    context = {
            'reviews' : reviews[index:index + show],
            'pages' : pno,
            'index' : page - 1,
            'category': Category.objects.all(),
            'tags': False,
            'pposts': reviews[:3] ,
            'activeapp':'REVIEWS'
        }
    return context

def get_catposts(category,show=5,page=1):
    cat  = Category.objects.filter(category=category).values('id')    
    posts = Review.objects.all().filter(category=cat[0]['id'],is_published=True).order_by('-date')    # Blog object quarry
    pno =range(int(posts.count()/show))   # range of pages 
    index = (page -1) * show #shat showin post from here 
    context = {
            'posts' : posts[index:index + show],
            'pages' : pno,
            'index' : page - 1,
            'current_category':category,
            'tags': False ,
            'pposts':False,
            'activeapp':'BLOG'
        }
    return context




# Create your views here.

def Index(request):
    return render(request,"public/reviews/review-index.html",get_allposts())



def Pages(request,pageno):
        return render(request,"public/reviews/review-index.html",context=get_allposts(page=pageno))


def ReviewByID(request,reviewid):
    
    review =  Review.objects.filter(id=reviewid).first()
    vk = review.get_all()
    return render(request,"public/reviews/review.html",context=vk)


def ReviewLike(request, reviewid):

    if request.user.is_authenticated:
        new_like, created = Like.objects.get_or_create(user=request.user,is_like=True, review_id=reviewid)
        if not created:
            return redirect(request.META.get('HTTP_REFERER'))
            # the user already liked this picture before
        else:
            new_like.save()
            # oll korrekt
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect("/login")

def ReviewDislike(request, reviewid):
    if request.user.is_authenticated:
        new_like, created = Like.objects.get_or_create(user=request.user,is_like=False, review_id=reviewid)
        if not created:
            return redirect(request.META.get('HTTP_REFERER'))
            # the user already liked this picture before
        else:
            new_like.save()
            # oll korrekt
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect("/login")

    