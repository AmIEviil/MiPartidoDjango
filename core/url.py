from unicodedata import name
from django.urls import path
from .views import home, centros ,info,inicioSesion,cerrar_sesion ,registro,videos
urlpatterns = [
    path('', home,name="home"),
    path('centros/', centros,name="centros"),
    path('info/', info,name="info"),
    path('inicioSesion/', inicioSesion,name="inicioSesion"),
    path('logout/', cerrar_sesion,name="logout"),
    path('registro/', registro,name="registro"),
    path('videos/',videos,name="videos"),
]
