from django.test import TestCase
from django.core.mail import send_mail 
import smtplib 
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def my_view(request):
    return render(request, "a_template.html", c)
# Recebendo email com smtplib 

# Fazendo conexão com o servidor do email 
servidor_email = smtplib.SMTP("smtp.google.com",587) 
servidor_email.starttls() 
with open('login.txt','r') as log:
    senha = log.read() 
servido_email.login('propostastrabalho123@gmail.com',senha)
'''
if str(request.method) == 'POST':
        form = email(request.POST)
        if form.is_valid() :
            form.send_email()
            messages.success(request, "Email enviado com sucesso")
            form = email()
        else:
            messages.error(request,"Não foi possivel enviar o email")
    else:
        form = email()
    teste = email()'''
