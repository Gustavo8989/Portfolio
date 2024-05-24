from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages 
from .forms import contatos 
# Create your views here.

def index(request):
    return render(request, 'polls/index.html')

def contato(request):
    if str(request.method) == 'POST':
        form = contatos(request.POST)
        if form.is_valid() :
            form.send_email()