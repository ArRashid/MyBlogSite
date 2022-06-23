
import imp
from django.shortcuts import redirect, render ,HttpResponse
from django.utils.translation import gettext_lazy as _

from Blog.models import *
from taggit.models import Tag,TaggedItem
from datetime import date



# main Variables 
allcat = Category.objects.all()
alltag = Tag.objects.all().order_by('-id')[:5]
promtpost = Posts.objects.order_by('-id')[:3]




# Main Mathods
def get_allposts(show=5,page=1):
    posts = Posts.objects.all().order_by('-date')             # Blog object quarry
    pno =range(int(posts.count()/show)+1)   # range of pages 
    index = (page -1) * show #shat showin post from here 
    context = {
            'posts' : posts[index:index + show],
            'pages' : pno,
            'index' : page - 1,
            'category': allcat ,
            'tags': alltag ,
            'pposts':promtpost,
            'activeapp':'BLOG'
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
            'current_category':category,
            'tags': alltag ,
            'pposts':promtpost,
            'activeapp':'BLOG'
        }
    return context




def get_tagposts(tag,show=5,page=1):
    tagid = Tag.objects.all().filter(name=tag).values('id')   
    pid = TaggedItem.objects.filter(tag_id=tagid[0]['id']).values('object_id')
    posts = Posts.objects.filter(id__in=pid)# Blog object quarry
    pno =range(int(posts.count()/show))   # range of pages 
    index = (page -1) * show #shat showin post from here 
    context = {
            'posts' : posts[index:index + show],
            'pages' : pno,
            'index' : page - 1,
            'category': allcat ,
            'tags': alltag ,
            'pposts':promtpost,
            'activeapp':'BLOG'
        }
    return context





# Create your views here.
def Index(request):
    if request.user.is_authenticated:
        return render(request,"private/blog/blog-index.html",context=get_allposts())
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


def Post(request,postno):
    post = Posts.objects.filter(id=postno)
    if  request.method == 'GET':
        
        comments = Comments.objects.all().order_by('date','id').filter(postid=postno)
        context = {
        'post': post[0],
        'comments':comments,
        'category': allcat,
        'tags':alltag,
        'pposts':promtpost,
        'activeapp':'BLOG'
            }
          
        return render(request,"public/blog/blog-post.html",context)
    else:
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']

        newcomment = Comments(name=name,email=email,comment=comment,postid=post[0],date=date.today())
        newcomment.save()
        return redirect('/blog/post/{0}'.format(postno))


def Tag_Post(request,tag,pageno=1):

    if request.user.is_authenticated:
        return HttpResponse("Welcome to special Blog")

    else:
        return render(request,"public/blog/blog-index.html",context=get_tagposts(tag=tag,page=pageno))
    
    
