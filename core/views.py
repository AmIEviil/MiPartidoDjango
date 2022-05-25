import email
from django.http import response
from django.shortcuts import render
from django.contrib import messages
# importar modelo de usuarios(User)
from django.contrib.auth.models import User
# importar librerias de validacion login
from django.contrib.auth import authenticate, logout, login
# importar librerira de decoradores que permite evitar el ingreso a paginas restringidas
from django.contrib.auth.decorators import login_required, permission_required

###########################################################################
# ------------------------------------------------------------------------------------
# incorporar las librerias necesarias para trabajar con la carga de datos
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
import json


def home(request):
    return render(request, 'core/principal.html')


def centros(request):
    return render(request, 'core/centros.html')


def info(request):
    return render(request, 'core/info.html')


def inicioSesion(request):
    if request.POST:
        nom_usuario = request.POST.get("txtUsuario")
        password = request.POST.get("txtPass")
        us = authenticate(request, username=nom_usuario, password=password)
        if us is not None and us.is_active:
            login(request, us)
            return render(request, "core/principal.html")
        else:
            contexto = {"mensaje": "no existe usuario o contraseña"}
            return render(request, "core/inicioSesion.html", contexto)
    return render(request, 'core/inicioSesion.html')

@login_required(login_url='/inicioSesion/')
def cerrar_sesion(request):
    logout(request)
    return render(request, "core/principal.html")

def registro(request):
    if request.POST:
        nom_usuario = request.POST.get("txtUsuario")
        correo = request.POST.get("txtCorreo")
        pass1 = request.POST.get("txtPass1")
        pass2 = request.POST.get("txtPass2")
        if pass1 != pass2:
            contexto = {"mensaje": "las contraseña no coinciden"}
            return render(request, "core/registro.html", contexto)
        try:
            usu = User.objects.get(username=nom_usuario)
            contexto = {
                "mensaje": "el nombre de usuario ya fue registrado, intente con otro"}
            return render(request, "core/registro.html", contexto)
        except:
            usu = User()
            usu.username = nom_usuario
            usu.email = correo
            usu.set_password(pass1)
            usu.save()
            us = authenticate(request, username=nom_usuario, password=pass1)
            login(request, us)
            messages.success(request, "Usuario creado correctamente")
            return render(request, "core/principal.html")
    return render(request, "core/registro.html")


def videos(request):
    return render(request,"core/videos.html")
