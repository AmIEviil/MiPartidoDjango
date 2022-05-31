from unicodedata import name
from django.urls import path
from .views import home, centros ,info,inicioSesion,cerrar_sesion ,registro,videos,selec_cancha,perfil
urlpatterns = [
    path('', home,name="home"),
    path('centros/', centros,name="centros"),
    path('info/', info,name="info"),
    path('inicioSesion/', inicioSesion,name="inicioSesion"),
    path('logout/', cerrar_sesion,name="logout"),
    path('registro/', registro,name="registro"),
    path('videos/',videos,name="videos"),
    path('selec_cancha/',selec_cancha,name="slc_cancha"),
    path('perfil/<str:username>/',perfil,name="perfil"),
]
