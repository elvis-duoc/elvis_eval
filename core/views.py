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
    return render(request, 'core/contacto.html')


def registro(request):
    return render(request, 'core/registro.html')


def iniciosesion(request):
    return render(request, 'core/iniciosesion.html')
