from django.urls import path
from . import views

urlpatterns= [
    path("",views.store, name="store"),
    path("cart/",views.cart, name="cart"),
    path("checkout/",views.checkout, name="checkout"),
    path("registrar/",views.registrar, name="registrar"),
    path("ingresar/",views.ingresar, name="ingresar"),
    path("salir/",views.salir, name="salir"),
]