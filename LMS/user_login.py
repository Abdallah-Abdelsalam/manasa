from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib import messages
from app.EmailBackEnd import EmailBackEnd
from app.models import Categories
from django.contrib.auth import authenticate,login,logout


def REGISTER(request):
    category = Categories.objects.all().order_by('id')[0:5]
    
    context ={
        'category':category,
    }

    if request.method == 'POST':

        username = request.POST.get("username")
        #password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        if User.objects.filter(email=email).exists():
            messages.warning(request,"Email Already Exists !")
            return redirect('register')
        

        #if User.objects.filter(username=username).exists():
         #   messages.warning(request,"Username Already Exists !")
          #  return redirect('register')
        
        
        user = User(
            first_name = username,
            username = email,
            last_name = phone,
        )
        #user.set_password(password)
        user.save()
        return redirect('home')

    return render(request,'registration/register.html',context)


def DO_LOGIN(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = EmailBackEnd.authenticate(
            request,
            username=email,
           )

        if user != None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Email and password are invalid !")
            return redirect("login")
        
def PROFILE(request):
    return render(request,'registration/profile.html')

def LOGOUT(request):
    logout(request)
    return redirect('home')

def PROFILE_UPDATE(request):
      if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        #password = request.POST.get('password')

        user_id = request.user.id

        user = User.objects.get(id=user_id)

        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        #if password != None and password != "":
           # user.set_password(password)
       # user.save()
        
        messages.success(request,'Profile Are Successfully Updated. ')
        return redirect('profile')

