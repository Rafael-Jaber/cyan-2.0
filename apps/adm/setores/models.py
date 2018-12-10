from django.db import models


class Setor(models.Model):
    dep_nome = models.CharField(max_length=80)
    dep_descricao = models.CharField(max_length=180)

    def __str__(self):
        return self.dep_nome
