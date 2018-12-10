import json
from django.shortcuts import render


def home(request):

    names = ['Teste 1', 'Teste 2']
    prices = ['500', '1000']

    context = {
        'names': json.dumps(names),
        'prices': json.dumps(prices),
    }

    return render(request, 'dash/index.html', context)


