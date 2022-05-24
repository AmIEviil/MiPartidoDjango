from django.urls import path
from .views import home, centros ,info,inicioSesion,registro
urlpatterns = [
    path('', home,name="home"),
    path('centros/', centros,name="centros"),
    path('info/', info,name="info"),
    path('inicioSesion/', inicioSesion,name="inicioSesion"),
    path('registro/', registro,name="registro"),
    
]
