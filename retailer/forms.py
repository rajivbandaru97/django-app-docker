from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from SBlokz.models import (User, Order, Product)
from manufacturer.models import Profile
from retailer.models import Profile2

class RetailerSignupForm(UserCreationForm):
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

class RetailerUpdateForm(forms.ModelForm):
    email =  forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email'] 

class Profile2UpdateForm(forms.ModelForm):

     class Meta:
         model = Profile2
         fields = ['image'] 