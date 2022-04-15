from tkinter import Widget
from django import forms
from .models import md_contact
class contact_form(forms.ModelForm):
    class Meta:
        model = md_contact
        fields=['name','mail','content']
        # Widget = {
        #     "name": forms.TextInput(attrs={"class":"input_class"})
        # }