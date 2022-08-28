from django.db import models
from django.utils.translation import gettext_lazy as _

class Categorias(models.TextChoices):
    INFORMATICA = 'INFO', _('Informática')
    GAMES = 'GAME', _('Games')
    ESPORTE = 'ESPO', _('Esporte')
    MODA = 'MODA', _('Moda')
    BELEAZA = 'BELE', _('Beleza')