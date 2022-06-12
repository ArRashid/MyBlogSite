
from django.shortcuts import render ,HttpResponse

from Blog.models import Posts

#Pos configuration
 
posts = Posts.objects.all()             # Blog object quarry
show = 5                                # per page blog show
pno =range(int(posts.count()/show)+1)   # range of pages 


# Create your views here.
def Index(request):
    if request.user.is_authenticated:
        return HttpResponse("Welcome to special Blog")
    else:  
        context = {
            'posts' : posts[0:0+ show],
            'pages' : pno,
            'index' : 0
        }
        return render(request,"public/blog/blog-index.html",context)

def Pages(request,no):
    if request.user.is_authenticated:
        return HttpResponse("Welcome to special Blog")

    else:
        pageindex = no - 1 # make index from get requ
        index  = pageindex * show # post index to show perticular posts in the pages 
        
        context = {
            'posts' : posts[index:index + show],
            'pages' : pno,
            'index' : pageindex
            
        }
        return render(request,"public/blog/blog-index.html",context)


    


