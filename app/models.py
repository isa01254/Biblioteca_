from django.db import models
class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name = "Nome da cidade")
    uf = models.CharField(max_length = 2, verbose_name = "UF")
    def __str__(self):
        return f"{self.nome}, {self.uf}"
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


class Autor(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome do autor")
    cidade =  models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade do autor")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
