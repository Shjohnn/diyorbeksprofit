from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View

class LoginView(View):
    def  get(self,request):
        return render(request,'login.html')

    def post(self,request):
        user =authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html')

class LogoutVeiw(View):
    def get(self,request):
        logout(request)
        return redirect('login')