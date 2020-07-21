from django.http import HttpResponse

def hello(request):
    return HttpResponse('Olá Mundo')

def funcao(request, nome):
    return HttpResponse('Seu nome é ' + str(nome))

def exemplo(request,ano, mes, dia):
    pass