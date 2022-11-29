
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Evento(models.Model):

    PUBLICO = (
        ('Aberto', 'Aberto'),
        ('Privado', 'Privado'),
    )

    PUBLICAR = (
        ('Não Publicado', 'Não Publicado'),
        ('Publicado', 'Publicado')
    )

    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    grupo = models.CharField(max_length=20)
    nome_empresa = models.CharField(max_length=50)
    nome_evento = models.CharField(max_length=50)
    data_inicio = models.DateTimeField(default=datetime.now(), blank=True)
    data_termino = models.DateTimeField(default=datetime.now(), blank=True)
    img = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    descricao = models.TextField()
    publico = models.CharField(max_length=20, choices=PUBLICO,)
    convidados_qtd = models.IntegerField()
    publicar = models.CharField(max_length=15, choices=PUBLICAR)
    nota_media = models.IntegerField(blank=True, default=0)
    soma_notas = models.IntegerField(blank=True,default=0)
    relatorios_feitos = models.IntegerField(blank=True, default=0)
    
    def __str__(self):
        return self.nome_evento

class Inscrito_Evento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    inscrito = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=40)
    email = models.CharField(max_length=50)

class Relatorio_Satisfacao(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    inscrito = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.IntegerField(blank=True)

    

