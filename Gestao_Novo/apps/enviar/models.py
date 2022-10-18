from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    e_mail = models.EmailField()
    grupo = models.CharField(max_length=100)

class RecuperarSenha(models.Model):
    email_r = models.EmailField()
    codigo = models.IntegerField(unique=True)
    data = models.DateTimeField(auto_now_add=True)
    data_vencimento = models.DateTimeField()