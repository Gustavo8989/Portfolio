from django import forms 
from django.core.mail import EmailMessage
import re 

class contatos(forms.Form):
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