
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login

class CustomCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']

# Create your views here.

def home(request):
    return render(request,'home.html')

def registration(request):
    if request.method == "POST":
        form = CustomCreateForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomCreateForm()
        context = {"form":form}
        return render(request,'registration.html',context)
    
def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form = AuthenticationForm()
        context = {"form":form}
        return render(request,'login.html',context)
       

