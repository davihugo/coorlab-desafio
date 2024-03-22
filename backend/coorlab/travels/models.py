from django.db import models

# Create your models here.

class Viagem(models.Model):
    id = models.AutoField(primary_key=True)
    nome_empresa = models.CharField(max_length=255)
    preco_conforto = models.DecimalField(max_digits=10, decimal_places=2)
    preco_econ = models.DecimalField(max_digits=10, decimal_places=2)
    cidade_destino = models.CharField(max_length=255)
    duracao = models.CharField(max_length=50)
    leito_econ = models.CharField(max_length=50)
    leito_conforto = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Viagem"
        verbose_name_plural = "Viagens"


    def __str__(self):
        return self.nome_empresa