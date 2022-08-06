from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from SBlokz.models import (User, Order, Product)
from manufacturer.models import Profile
from retailer.models import Profile2
from simple_search import search_form_factory

class ManufacturerSignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
       user = super().save(commit=False)
       user.is_manufacturer = True
       if commit:
           user.save()
       return user
 
class ManufacturerUpdateForm(forms.ModelForm):
    email =  forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']  


class ProfileUpdateForm(forms.ModelForm):

     class Meta:
         model = Profile
         fields = ['image'] 

SearchForm = search_form_factory(Order.objects.all(), ['hash_id'])