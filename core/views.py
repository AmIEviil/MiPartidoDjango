from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'core/principal.html')

def centros(request):
    return render(request, 'core/centros.html')

def info(request):
    return render(request, 'core/info.html')

def inicioSesion(request):
    return render(request, 'core/inicioSesion.html')

def registro(request):
    return render(request, 'core/registro.html')