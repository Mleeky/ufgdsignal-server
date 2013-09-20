'''
Created on 18/09/2013

@author: HelderSi
'''
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import AnuncianteProfile

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

class AnuncianteForm(ModelForm):
    class Meta:
        model = AnuncianteProfile
        fields = ('cpf','cargo')