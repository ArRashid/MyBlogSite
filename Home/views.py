
from email import message
from django.shortcuts import render,HttpResponse,redirect
from Home.models import *
from django.contrib.auth import authenticate, login,logout
from users.models import CustomUser
from django.http import FileResponse, Http404

# Create your views here.

def Index(request):
    features = Features.objects.all()
    context={
        'features':features,
        'activeapp':'HOME'
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


def MySelf(request):


    if request.method == "POST":
       
       newcontact = ContactMe(name=request.POST['name'],subject=request.POST['subject'],email=request.POST['email'],message=request.POST['message'] )
       newcontact.save()
       return redirect("/myself")

    
    else:
        context  ={
            'certificates' :  MyCertificate.objects.all()
        }
        return render(request,"public/myself.html",context)

def GetCv(request):
   
      
    return FileResponse(open('STATIC/myself/cv/AbdurRashidMondal.pdf', 'rb'), content_type='application/pdf')
    try:
        pass
    except FileNotFoundError:
        raise Http404()



