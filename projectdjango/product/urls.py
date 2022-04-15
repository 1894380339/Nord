from django.urls import path
from . import views
app_name = 'product'
urlpatterns = [
    path('', views.productView, name="url_products"),
    path('categary', views.category.as_view(), name="url_category"),
    path('<int:id>', views.product_detail, name="url_product_detail"),
    
]