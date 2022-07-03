
from operator import truediv
from django.shortcuts import redirect, render,HttpResponse
from datetime import date


# Create your views here.
from  .forms import *

def Index(request):
     context = {
          "CreatePost": CreatePost()
     }
     return render(request,"dashboard-base.html",context=context)


def AddPost(request):
     if request.user.is_authenticated :

          if request.method == 'POST':
               form = CreatePost(request.POST, request.FILES)
               if form.is_valid():
                    post = form.save(commit=False)
                    post.author = request.user
                    post.date = date.today()
                    post.save()
                    return HttpResponse('Post Added successfully')

          context = {
               "CreatePost": CreatePost()
           }
          return render(request,"private/dashboard/addpost.html",context=context)
    
     




def EditePost(request):
     if request.user.is_authenticated :
          posts = list(Posts.objects.filter(author=request.user).all().order_by('-id'))
          context = {
               "Posts": posts,
          }
          return render(request,"private/dashboard/editepost.html",context)
     else:
          return HttpResponse("You are not athorised")


def PostEditor(request,postid):
     instance = Posts.objects.get(id=postid)


     if request.user.is_authenticated and request.user == instance.author:
         
          form = CreatePost(request.POST or None, instance=instance )

          if request.method == 'POST' :
               form = CreatePost(request.POST, request.FILES,instance=instance)  
               if form.is_valid():  
                    form.instance.mdate = date.today()
                    form.save()
                    return redirect("/dashboard/editepost")
          else:
          
               context = {
               "CreatePost": form
               }
               return render(request,"private/dashboard/posteditor.html",context)

     else:
          return HttpResponse("You are not athorised")


def DeletePost(request,postid):
     instance = Posts.objects.get(id=postid)


     if request.user.is_authenticated and request.user == instance.author:
          instance.delete()
          return redirect("/dashboard/editepost")
          
     else:
          return HttpResponse("You are not athorised")



     

def PublishPost(request,postid):
     instance = Posts.objects.get(id=postid)


     if request.user.is_authenticated and request.user == instance.author:
         
          instance.is_published = True
          instance.save()
          return redirect("/dashboard/editepost")
          
     else:
          return HttpResponse("You are not athorised")  


def UnpublishPost(request,postid):
     instance = Posts.objects.get(id=postid)

     if request.user.is_authenticated and request.user == instance.author:
         
          instance.is_published = False
          instance.save()
          return redirect("/dashboard/editepost")
          
     else:
          return HttpResponse("You are not athorised")   