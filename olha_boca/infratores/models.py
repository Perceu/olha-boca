from django.db import models


class Infratores(models.Model):
    
    class Meta:
        verbose_name = "Infrator"
        verbose_name_plural = "Infratores"

    nome = models.CharField(max_length=150)
    setor = models.CharField(max_length=150)

    def __str__(self):
        return self.nome