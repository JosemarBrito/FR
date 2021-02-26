from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse('Filhas do Rei, o melhor lugar para voc~e compras suas roupas evangelicas'
                        'Venha conferir')
