from django.db import models
from django.contrib.auth.models import User
from apps.adm.setores.models import Setor


class Usuario(models.Model):
    fun_nome = models.CharField(max_length=150)
    fun_user = models.OneToOneField(User, on_delete=models.PROTECT)
    fun_celular = models.CharField(max_length=15)
    fun_gerente = models.BooleanField(default=False)
    fun_setor_id = models.ManyToManyField(Setor)

    def __str__(self):
        return self.fun_nome
