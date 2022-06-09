from django.shortcuts import render ,HttpResponse

# Create your views here.
def Index(request):

    if request.user.is_authenticated:
        return HttpResponse("Welcome to special Blog")

    else:
        return HttpResponse("Welcome to Blog")