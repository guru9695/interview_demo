from django.forms import ModelForm
from django import forms
from .models import *


class addpro(forms.ModelForm): 
    class Meta: 
        model = Item 
        fields =['image']