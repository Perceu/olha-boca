from django.db import models
from olha_boca.infratores.models import Infratores
# Create your models here.

class InfracoesTipos(models.Model):

    class Meta:
        verbose_name = "Tipo de Infração"
        verbose_name_plural = "Tipos de Infrações"

    tipo = models.CharField(max_length=50)
    vibs = models.IntegerField(verbose_name='VIBS(valor por infração de boca suja)', default=1)
    multiplicador_vibs = models.IntegerField(verbose_name='multiplicador do VIBS(1VIBS = 1R$)', default=1)

    def __str__(self):
        return self.tipo

        
class Infracoes(models.Model):

    class Meta:
        verbose_name = "Infração"
        verbose_name_plural = "Infrações"

    pessoa = models.ForeignKey(Infratores, on_delete=models.CASCADE, related_name="infracoes")
    tipo = models.ForeignKey(InfracoesTipos, on_delete=models.RESTRICT, related_name="infracoes")
    paga = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pessoa}:{self.tipo}"