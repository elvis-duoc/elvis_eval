from django import forms
from django.forms import ModelForm, fields
from .models import Contacto, Login


class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ['usuario', 'password']


class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'mensaje']
