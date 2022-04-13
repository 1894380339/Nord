from django.shortcuts import render

# Create your views here.
from itertools import product
from aiohttp import RequestInfo
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render,redirect
from django.contrib import messages
from django.views import View
from cart.models import *
from order.models import Order
# Create your views here.
def Cart_view(request):
    if request.user.is_authenticated:
        customer = request.user
        cart, create = Cart.objects.get_or_create(user=customer)
        items = cart.cartitem_set.all()
    else: 
        cart=[]
        items=[]
    context = {'items':items,'cart':cart}
    return render(request, 'homepage/cart.html', context)


class Add_order(View):
    def post(self,request):
        if request.method == "POST":
            order = Order()
            order.user = request.user
            cart = Cart.objects.get(pk=request.POST["cart_id"])
            order.cart= cart
            # order.subtotal = request.POST["subtotal"]
            order.phone = request.POST["phone"]
            order.shiping_address = request.POST["address"]
            order.save()
            return redirect("/cart")
class Add_to_cart(View):
    def post(self,request):
        id = request.POST.get("productid")
        product = Product.objects.get(id=id)
        if request.user.is_authenticated:
            customer = request.user
            cart, create = Cart.objects.get_or_create(user=customer, is_completed=False)
            variation = Variation.objects.get(id=id)
            cartItem, create = CartItem.objects.get_or_create(cart=cart, product=product, item=variation)
            cartItem.save()
        return redirect("/cart")