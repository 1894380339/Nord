from django.shortcuts import render
# Create your views here.
from .models import Product, Category
from django.views import View


def productView(request):
    categorys =Category.objects.all()
    products = Product.objects.all()
    return render(request, 'homepage/product.html', {'products':products,'categorys':categorys})

class category(View):
    def post(self,request):
        if request.method=="POST":
            categorys = Category.objects.all()
            category = Category.objects.get(id=request.POST["category_id"])
            products = Product.objects.filter(category=category)
            return render(request, 'homepage/product.html', {'products':products,'categorys':categorys})

def product_detail(request,id):
    product = Product.objects.get(pk=id)
    return render(request, 'homepage/product_detail.html', {'product':product})