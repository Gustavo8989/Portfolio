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
            messages.success(request, "Email enviado com sucesso")
            form = contatos()
        else:
            messages.error(request,"Não foi possivel enviar o email")
    else:
        form = contatos()
    context = {
        "form":form
        }
        
    return render(request,"contato.html",context)