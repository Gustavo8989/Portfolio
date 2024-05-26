from django.test import TestCase
from django.core.mail import send_mail 


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