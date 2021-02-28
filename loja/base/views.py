from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse('<h1>Filhas do Rei, o melhor lugar para você compras suas roupas evangelicas'
                        'Venha conferir</h1>')
