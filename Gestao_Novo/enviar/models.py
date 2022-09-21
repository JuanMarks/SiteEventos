from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    e_mail = models.EmailField()
    grupo = models.CharField(max_length=100)
    