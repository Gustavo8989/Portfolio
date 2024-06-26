from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages 
from .forms import email
import re  
# Create your views here.

def index(request):
    return render(request, 'polls/index.html')

def contato(request):
    teste = email()
    return render(request,"polls/contato.html",{'teste':teste})