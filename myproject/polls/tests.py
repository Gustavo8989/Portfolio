from django.test import TestCase
import re 
# Create your tests here.
email = "aragorn122334gmail.com"
padra_email = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
resultado = re.search(padra_email,email)
if resultado:
    print("Email valido")
else:
    print("Email invalido")