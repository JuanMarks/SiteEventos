from django.db import models

# Create your models here.

class Arquivo_excel(models.Model):
    arquivo = models.FileField(upload_to='static/Arquivo/%d/%m/%Y/')