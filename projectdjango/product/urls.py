from django.urls import path
from . import views
app_name = 'product'
urlpatterns = [
    path('', views.productView, name="url_products"),
    path('categary', views.category.as_view(), name="url_category"),
    
]