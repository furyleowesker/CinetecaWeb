from django.shortcuts import render
from sistema_venta.models import Funcion, Boleto

# Create your views here.
def bienvenida(request):
    numero_funciones = Funcion.objects.count()
    funciones = Funcion.objects.order_by('id')
    numero_boletos = Boleto.objects.count()
    boletos = Boleto.objects.order_by('id')
    return  render(request, 'bienvenida.html', {'numero_funciones':numero_funciones, 'funciones':funciones, 'numero_boletos':numero_boletos, 'boletos':boletos})


def login(request):
    return render(request, 'login.html')


def usuario(request):
    return render(request, 'usuario.html')


def cartelera(request):
    return render(request, 'cartelera.html')


def dulceria(request):
    return render(request, 'dulceria.html')
