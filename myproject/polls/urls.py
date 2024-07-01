from django.urls import path
from django.http import HttpResponse
from . import views 

urlpatterns = [
    path("home", views.index, name="index"),
    path("contato",views.contato, name="contato"),
    path("Email", views.email_success,name="email_success") 
]
