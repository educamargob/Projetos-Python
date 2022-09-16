from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from produtos.models.categoria import Categorias


class Produtos(models.Model):
    nome_produto = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50,choices=Categorias.choices, default=0)
    preco = models.FloatField()
    descricao = models.CharField(max_length=70)
    data_criacao = models.DateTimeField(default=datetime.now, blank=True)
    foto_produto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    def __str__(self):
        return self.nome_produto

