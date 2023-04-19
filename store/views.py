from django.shortcuts import render, redirect
from store.models import *
from django.contrib import messages
from .form import UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

def salir(request):
    logout(request)
    messages.success(request, "Sesion Cerrada")
    return redirect("ingresar")

def ingresar(request):
    if request.method=="POST":
        form=AuthenticationForm(request, request.POST)
        if form.is_valid():
            nombreUsuario=form.cleaned_data.get("username")
            contraseña=form.cleaned_data.get("password")
            usuario=authenticate(username=nombreUsuario, password=contraseña)
            if usuario is not None:
                login(request, usuario)
                messages.success(request,"Bienvenido nuevamente %s" %nombreUsuario)
                return redirect("store")
            else:
                messages.error(request, "El usuario o contraseña son incorrectos")
        else:
            messages.error(request, "El usuario o contraseña son incorrectos")
    else:
        form=AuthenticationForm()
        context={"formulario":form}
        return render(request, "store/login.html",context)

def registrar(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data["username"]
            messages.success(request, "Usuario %s Creado Correctamente" %username)
    else:
        form=UserRegisterForm()
    context={"formulario":form}
    return render(request, "store/registrar.html",context)

def store(request):
    context={
        'productos':Product.objects.all()
    }
    return render(request, "store/store.html",context)

def cart(request):
    context={}
    return render(request, "store/cart.html",context)

def checkout(request):
    context={}
    return render(request,"store/checkout.html",context)