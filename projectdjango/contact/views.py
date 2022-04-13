from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import contact_form
from django.contrib import messages
from django.views import View
from rest_framework.response import Response
# Create your views here.
# def contact_view(request):
#     ct = contact_form()
#     return render(request,"contact/form_contact.html", {"ct":ct})

class class_contact(View):
    def get(self, request):
        ct = contact_form()
        return render(request,"homepage/contact.html", {"ct":ct})

    def post(self,request):
        if request.method == "POST":
            pf = contact_form(request.POST)
            if pf.is_valid():
                pf.save()
                messages.success(request, 'Form submission successful')
                # messages.success(request, 'Form submission successful',extra_tags='alert alert-success alert-dismissible fade show')
                return render(request,"homepage/contact.html",{"ct":pf})