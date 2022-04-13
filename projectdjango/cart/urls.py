from django.urls import path
from . import views
from .views import *
app_name = 'cart'
urlpatterns = [
    path('', views.Cart_view, name="url_cart"),
    path('add', views.Add_order.as_view(), name="url_add"), 
    path('addtocart', views.Add_to_cart.as_view(), name="url_addtocart"),    

]