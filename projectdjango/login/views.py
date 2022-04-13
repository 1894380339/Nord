from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login
from requests import request
from user.models import CustomerUser
# Create your views here.
class class_login(View):
    def get(self, request):
        return render(request,'homepage/login.html')
    def post(self, request):
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user =authenticate(request, username=username, password=password)
            if user is None:
                return render(request,"homepage/login.html",{"context":"Invalid User"})
            login(request,user)
            # return redirect('/')
            return render(request,"homepage/index.html",{"username":f'hi, {username}'})



class class_singup(View):
    def post(self,request):
        if request.method == "POST":
            password = request.POST["password"]
            password2 = request.POST["password2"]
            username = request.POST["username"]
            email = request.POST["mail"]
            if (password==password2) is True:
                user=CustomerUser()
                user.username = username
                user.email=email
                user.set_password(password)
                user.save()
                return render(request,"homepage/index.html")
            else:
                return redirect("/login")

