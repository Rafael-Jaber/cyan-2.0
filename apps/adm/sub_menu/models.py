from django.db import models


class SubMenu(models.Model):
    sub_nome = models.CharField(max_length=80)
    sub_url_name = models.CharField(max_length=150)
    sub_icon_class = models.CharField(max_length=150)

    def __str__(self):
        return self.sub_nome
