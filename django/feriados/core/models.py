from django.db import models

class FeriadoModel(models.Model):
    nome = models.CharField('Feriado', max_length=50)
    dia = models.IntegerField('Data')
    mes = models.IntegerField('Mes')
    modificado_em = models.DateTimeField(verbose_name='modificado em', auto_now_add=False, auto_now=True)