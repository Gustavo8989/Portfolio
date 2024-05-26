from django.db import models
from django import forms 
from django.core.mail import EmailMessage
from django.http import HttpResponse
import re 
import qrcode 

class email(forms.Form):
    nome = forms.CharField(label="Nome",max_length=50)
    email = forms.EmailField(label="Email",max_length=100)
    assunto = forms.CharField(label="Assunto",max_length=100)
    menssagem = forms.CharField(label="Menssagem",widget=forms.Textarea())
    def enviando_email(self):
        nome = self.cleaned_data['Nome']
        email = self.cleaned_data['email'] 
        assunto = self.cleaned_data['assunto']
        menssagem = self.cleaned_data['messagem'] 
        corpo_email = f"Nome:{nome}\nMenssagem{menssagem}"
        verificando_email = verificando_email()
        mail = EmailMessage(
            subject=assunto,
            para_email='gustavohenriquealves418@gmail.com',
            to=[email,],
            body=corpo_email,
            headers={
                'Replat-to':'gustavohenriquealves418@gmail.com'
            }
        )
        mail.send()
    def verificando_email(self):
        padra_email = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        resultado = re.search(padra_email,self.email)
        if resultado:
            return HttpResponse("Email valido")
        else:
            return HttpResponse("Email invalido")
