from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Mensagens(models.Model):
    titulo = models.CharField(max_length=100)
    corpo_mensagem = models.CharField(max_length=126)
    icon = models.ImageField(upload_to='foto-mensagem', blank=True)
    data_criacao = models.DateTimeField(default=datetime.now, blank=True)
    habilitada = models.BooleanField(default=False)