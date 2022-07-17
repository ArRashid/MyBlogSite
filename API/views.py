
import imp
from re import T
from unicodedata import category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date
# importing data and serializer
from .seri import *
from Blog.models import Posts


# Create your views here.




@api_view(['GET', 'POST'])
def Test(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "API test  successfull, It's working fine!"})




@api_view(['GET', 'POST'])
def BlogPosts(request):
    if request.method == 'GET':
        qset  = Posts.objects.all()
        sliz = PostSeri(qset,many=True)
        return Response(sliz.data)
    elif request.method == 'POST':
        apikey = request.data['apikey']
        if apikey == 'ok':
            title = request.data['title']
            content = request.data["content"]
            author = request.data["author_id"]
            category  = request.data["category_id"]
            newpost = Posts(title=title,content=content,author_id=author,category_id=category,date=date.today())
            newpost.save()    
            return Response({"Resultcode": 0,"message": "Data saved successfully", "your data": request.data})
        else:
            return Response({"Resultcode": 1,"message": "You are not authorized"})

@api_view(['GET', 'POST','DELETE'])
def BlogPost(request,pk):
    if request.method == 'GET':
        qset  = Posts.objects.first()
        print(qset)
        sliz = PostSeri(qset)
        return Response(sliz.data)

    elif request.method == 'POST':
        apikey = request.data['apikey']
        if apikey == 'ok':
            title = request.data['title']
            content = request.data["content"]
            author = request.data["author_id"]
            category  = request.data["category_id"]
            newpost = Posts(id=pk,title=title,content=content,author_id=author,category_id=category,date=date.today())
            newpost.save()    
            return Response({"Resultcode": 0,"message": "Data saved successfully"})
        
        else:
            return Response({"Resultcode": 1,"message": "You are not authorized"})

    elif request.method == 'DELETE':
        apikey = request.data['apikey']
        if apikey == 'ok':
            res = Posts.objects.filter(id=pk)
            res.delete()
            return Response({"Resultcode": 0,"message": "Data delete successfully"})
        else:
            return Response({"Resultcode": 1,"message": "You are not authorized"})

