from django import forms
from core.forms import ContactoForm, LoginForm
from core.models import Login, Contacto
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'core/index.html')


def pez(request):
    return render(request, 'core/pez.html')


def portalapiz(request):
    return render(request, 'core/portalapiz.html')


def fuente(request):
    return render(request, 'core/fuente.html')


def contacto(request):
    datos = {
        'form1': ContactoForm
    }
    if request.method == "POST":
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Mensaje Enviado Correctamente"
    return render(request, 'core/contacto.html', datos)


def registro(request):
    datos = {
        'form': LoginForm
    }
    if request.method == "POST":
        formulario = LoginForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['estado'] = "Datos Guardados con EXITO"
    return render(request, 'core/registro.html', datos)


def iniciosesion(request):
    return render(request, 'core/iniciosesion.html')
