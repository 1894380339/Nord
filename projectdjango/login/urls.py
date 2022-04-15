from django.urls import path
from . import views
app_name = 'login'
urlpatterns = [
    path('',views.class_login.as_view(), name="url_login"),
    path('singup',views.class_singup.as_view(), name="url_singup"),
]