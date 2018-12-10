from django.db import models


class Modulo(models.Model):
    mod_nome = models.CharField(max_length=30)
    mod_descricao = models.CharField(max_length=150)
    mod_url_name = models.CharField(max_length=200)

    def __str__(self):
        return self.mod_nome
