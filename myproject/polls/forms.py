from django import forms 
import re 

class contatos(forms.Form):
    nome = forms.CharField(label="Nome",max_length=50)
    email = forms.EmailField(label="Email",max_length=100)
    assunto = forms.CharField(label="Assunto",max_length=100)
    menssagem = forms.CharField(label="Menssagem",widget=forms.Textarea())
    def enviando_email(self):
        pass  