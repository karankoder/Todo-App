from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from TaskHive.models import Taskdb
from django.contrib import messages


def homepage(request):
    if request.user.is_authenticated:
        return redirect('mainpage')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        myuser=authenticate(username=username,password=password)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Logged in successfully")
            return redirect('mainpage')
        else:
            messages.error(request,"Username or password is incorrect")
            return redirect('/')
    return render(request,'TaskHive/homepage.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('mainpage')
    if request.method== 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if(User.objects.filter(username=username)):
            messages.success(request,"Username already exists!")
            return redirect('signup')
        if(User.objects.filter(email=email)):
            messages.success(request,"Email already exists!")
            return redirect('signup')
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        messages.success(request,"User Created Successfully")
        return redirect('mainpage')
    return render(request,'TaskHive/signup.html')

@login_required(login_url='/')
def mainpage(request):
    tasks=Taskdb.objects.filter(user=request.user)
    return render(request,'TaskHive/mainpage.html',{'tasks':tasks})

def addtodo(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            title=request.POST.get('title')
            if(title!=""):
                new_task=Taskdb(title=title,user=request.user)
                new_task.save()
                messages.success(request,"Task added successfully")
            else:
                messages.error(request,"Title can't be empty")
            return redirect('mainpage')
            
    
def user_logout(request):
    logout(request)
    return redirect('/')

def delete_task(request,id):
    Taskdb.objects.get(pk=id).delete()
    messages.success(request,"Task deleted Successfully")
    return redirect('mainpage')




# Create your views here.
