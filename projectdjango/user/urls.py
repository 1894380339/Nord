from django.urls import path
from . import views
app_name = 'user'
urlpatterns = [
    path('', views.view_user.as_view(), name="url_user"),
]