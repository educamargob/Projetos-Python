from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    cnpj = models.CharField(max_length=14)
    data_criacao = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.nome
