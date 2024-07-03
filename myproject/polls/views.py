from django.views.decorators.csrf import csrf_protect 
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .forms import email

import re  
# Create your views here.

def index(request):
    return render(request, 'polls/index.html')

def contato(request):
    formulario = email()
    return render(request,"polls/contato.html",{'formulario':formulario})

def email_success(request):
    return render(request,'polls/email_success.html')


