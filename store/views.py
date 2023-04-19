from django.shortcuts import render
from store.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import UserRegisterForm

def registrar(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
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