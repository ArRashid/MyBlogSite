
from django.shortcuts import render,HttpResponse
from datetime import date


# Create your views here.
from  .forms import *

def Index(request):
     context = {
          "CreatePost": CreatePost()
     }
     return render(request,"dashboard-base.html",context=context)


def AddPost(request):
    
     if request.method == 'POST':
          form = CreatePost(request.POST, request.FILES)
          if form.is_valid():
               post = form.save(commit=False)
               post.author = request.user.name
               post.date = date.today()
               post.save()
               return HttpResponse('Post Added successfully')
          
        

     context = {
          "CreatePost": CreatePost()
     }
     return render(request,"private/dashboard/addpost.html",context=context)




def EditePost(request):
     print()
     posts = list(Posts.objects.all().order_by('-date'))

     context = {
          "Posts": posts,
     }
     return render(request,"private/dashboard/editepost.html",context)


def PostEditor(request,postid):

     instance = Posts.objects.get(id=postid)
     form = CreatePost(request.POST or None, instance=instance )



     if request.method == 'POST':
          form = CreatePost(request.POST, request.FILES,instance=instance)  
          if form.is_valid():  
               form.instance.mdate = date.today()
               form.save()

              
               
               return HttpResponse('You post has be updated')
     else:
          
          context = {
          "CreatePost": form
          }
          return render(request,"private/dashboard/posteditor.html",context)
     