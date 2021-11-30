from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenida(request):
    return HttpResponse('Bienvenido a la pagina de Cineteca')
