from django.db import models
from apps.adm.modulos.models import Modulo
from apps.adm.sub_menu.models import SubMenu


class Menu(models.Model):
    men_nome = models.CharField(max_length=80)
    men_module = models.ForeignKey(Modulo, on_delete=models.PROTECT)
    men_url_name = models.CharField(max_length=150)
    men_icon_class = models.CharField(max_length=150)
    men_submenu = models.ManyToManyField(SubMenu, blank=True, null=True)

    def __str__(self):
        return self.men_nome
