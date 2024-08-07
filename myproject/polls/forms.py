from django.db import models 
from django import forms 
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import FileResponse 
from . import views 
import smtplib
import re 


class email(forms.Form):
    nome = forms.CharField(label="Nome",max_length=50)
    email = forms.EmailField(label="Email",max_length=100)
    menssagem = forms.CharField(label="Menssagem",widget=forms.Textarea())
    def corpo_email(self):
        nome = self.cleaned_data['Nome']
        email = self.cleaned_data['email'] 
        assunto = self.cleaned_data['assunto']
        menssagem = self.cleaned_data['messagem'] 
        corpo_email = f"Nome:{nome}\nMenssagem{menssagem}"
        verificando_email = verificando_email(self.email)
        mail = EmailMessage(
            subject=assunto,
            para_email='propostastrabalho123@gmail.com',
            to=[email],
            body=corpo_email,
            headers={
                'Replat-to':'propostastrabalho123@gmail.com'
            }
        )
        mail.send()
        self.proposta_email = request.POST.get(mail) 
        print(self.proposta_email) 
    def output_button(self):
        self.proposta_email 


    def verificando_email(self):
        padra_email = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        resultado = re.search(padra_email,self.email)
        if resultado:
            return HttpResponse("Email valido")
        else:
            return HttpResponse("Email invalido")
