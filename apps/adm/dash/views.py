import json
from django.shortcuts import render
from apps.adm.modulos.models import Modulo
from apps.adm.menu.models import Menu


def home(request):
    menuItens = Menu.objects.filter(men_module=1)

    names = ['Teste 1', 'Teste 2']
    prices = ['500', '1000']

    context = {
        'menus': menuItens,
        'names': json.dumps(names),
        'prices': json.dumps(prices),
    }

    return render(request, 'dash/index.html', context)


