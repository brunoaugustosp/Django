from django.http import HttpResponse
from django.shortcuts import render,redirect


def hello(request):
    nome = 'Bruno ALOO'
    return render(request, 'index.html', {'nome': nome})


def funcao(request, nome):
    return HttpResponse('Seu nome é ' + str(nome))

def exemplo(request,ano, mes, dia):
    pass