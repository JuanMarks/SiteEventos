from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nome_completo = models.CharField(max_length=100)
    nome_usuario = models.CharField(max_length=40)
    telefone = models.CharField(max_length=20)
    grupo = models.CharField(max_length=30)
    nome_empresa = models.CharField(max_length=30)
    email = models.EmailField()

class Empresa(models.Model):
    nome_completo = models.CharField(max_length=200)
    nome_empresa = models.CharField(max_length=30)
    telefone = models.CharField(max_length=100)
    email = models.EmailField()