from importlib.resources import contents

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import datetime
import time

def index(request):
    template = loader.get_template("sports/index.html")
    context = get_context('Главная страница')
    return HttpResponse(template.render(context, request))

def sport(request, sport_name):
    template = loader.get_template("sports/sport.html")
    context = get_context(sport_name,{'text': f'Новости {sport_name}'
                         })
    return HttpResponse(template.render(context, request))

def daytime(request):
    template = loader.get_template("sports/daytime.html")
    if datetime.datetime.now().time().hour <= 6:
        text = 'доброй ночи'
    elif datetime.datetime.now().time().hour <= 12:
        text = 'доброе утро'
    elif datetime.datetime.now().time().hour <= 18:
        text = 'добрый день'
    else:
        text = 'добрый вечер'
    t = {'time': time.strftime("%H:%M:%S", time.localtime()),
         'daytime': text}
    context = get_context ('Время', t)
    return HttpResponse(template.render(context, request))

def get_context(title, d=None):
    context = {'title': title,
               'pages': [('football', 'Футбол'),
                         ('basketball', 'Баскетбол'),
                         ('hockey', 'Хоккей'),
                         ('daytime/', 'время')
                         ]}
    if d:
        for k in d:
            context[k] = d[k]
    return context