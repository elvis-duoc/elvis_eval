from django.urls import path
from .views import home, pez, portalapiz, fuente, contacto, registro, iniciosesion

urlpatterns = [
    path('', home, name="index"),
    path('pez', pez, name="pez"),
    path('portalapiz', portalapiz, name="portalapiz"),
    path('fuente', fuente, name="fuente"),
    path('contacto', contacto, name="contacto"),
    path('registro', registro, name="registro"),
    path('iniciosesion', iniciosesion, name="iniciosesion"),
]
