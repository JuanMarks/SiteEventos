from django.db import models

# Create your models here.

class Evento(models.Model):
    PUBLICO = (
        ('Aberto', 'Aberto'),
        ('Privado', 'Privado'),
    )
    nome_evento = models.CharField(max_length=200)
    img = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    descricao = models.TextField()
    publico = models.CharField(
        max_length=20,
        choices=PUBLICO,
        )
    convidados_qtd = models.IntegerField()
    habilitar_inscrever = models.BooleanField(default=False)
    def __str__(self):
        return self.nome_evento
    
class Cadastro_Evento(models.Model):
    nome_evento = models.ForeignKey(Evento,on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    cpf_cnpj = models.CharField(max_length=20)
    email = models.EmailField()

