from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from cadastro_clientes.models.estados import Estados


class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=100)
    endereco = models.CharField(max_length=70)
    bairro = models.CharField(max_length=70)
    cidade = models.CharField(max_length=70)
    estado = models.CharField(max_length=50,choices=Estados.choices, default=0)
    cep = models.CharField(max_length=9)
    cnpj = models.CharField(max_length=19)
    data_criacao = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.nome

