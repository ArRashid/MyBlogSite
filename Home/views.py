
from django.shortcuts import render,HttpResponse,redirect
from Home.models import Features
from django.contrib.auth import authenticate, login,logout
from users.models import CustomUser


# Create your views here.

def Index(request):
    features = Features.objects.all()
    context={
        'features':features
        }
    if request.user.is_authenticated:
        return render(request,"private/index.html",context)
    else:
      return render(request,"public/index.html",context)



def Login(request):
    if request.method == "POST":
        email = request.POST['email']
        password =  request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect("/")
        else:
            # Return an 'invalid login' error message.
            return HttpResponse("invalide user id or pass")
    else:
        return render(request,"public/login.html")

def Logout(request):
    logout(request)
    return redirect("/")

def Registration(request):
    if request.method == "POST":
        pfp = request.POST['pfp']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 =  request.POST['password2']

        user = CustomUser.objects.create_user(pfp=pfp,name=name,phone=phone,email=email, password=password1)
        user.save()
        login(request, user)
        return redirect("/")
    else:
        return render(request,"public/registration.html")

    
   



def Check_user_login_or_not(request):
    if request.user.is_authenticated:
    # do something if the user is authenticated
      return HttpResponse("is user logged in")
    else:
      return HttpResponse("no user loged in")

