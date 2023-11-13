from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserInfo


def loginPage(request):
   
   if request.method == "POST":
      username = request.POST.get("username")
      password = request.POST.get("password")
      
      user = authenticate(username=username, password=password)
      if user is not None:
         login(request,user)
         return redirect("indexPage")
      
   
   context={}
   return render(request,'user/login.html', context)

def registerPage(request):

   if request.method == "POST":
      fname = request.POST.get("fname")
      lname = request.POST.get("lname")
      username_email = request.POST.get("username_email")
      password1 = request.POST.get("password1")
      password2 = request.POST.get("password2")
      birthdate = request.POST.get("birthdate")
      address1 = request.POST.get("address1")
      address2 = request.POST.get("address2")
      city = request.POST.get("city")
      mobile = request.POST.get("mobile")
      
      user_bl = usercom_bl = True
      if User.objects.filter(username=username_email).exists():
         user_bl = False

      if not (".com" in username_email):
         usercom_bl = False
         
      if password1 == password2 and user_bl and usercom_bl:
         user = User.objects.create_user(username=username_email, email=username_email, password=password1, first_name=fname, last_name=lname)
         user.save()
         
         userinfo = UserInfo(user=user,birthdate=birthdate, address1=address1, address2=address2, city=city, mobile=mobile)
         userinfo.save()
   
         return redirect("loginPage")
   context={}
   return render(request,'user/register.html', context)


@login_required(login_url="loginPage")
def passwordChangePage(request):
   context={}
   return render(request,'user/password-change.html', context)


@login_required(login_url="loginPage")
def logoutUser(request):
   logout(request)
   return redirect("loginPage")