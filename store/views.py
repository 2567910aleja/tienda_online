from django.shortcuts import render
from store.models import *

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