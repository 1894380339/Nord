from django.shortcuts import render
from .views import View

def view_user(request):
    if request.user.is_authenticated:
        customer = request.user
        username = customer.username
        return render(request, 'homepage/cart.html',{"user":customer,"username":username})
    