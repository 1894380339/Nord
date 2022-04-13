from django.urls import path
from . import views
app_name = 'contact'
urlpatterns = [
    path('', views.class_contact.as_view(), name="view_contact"),
]