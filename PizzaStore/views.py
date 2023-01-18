from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def store (request):
    return HttpResponse("<h1>PizzaStore</h1>")

def formulario(request):
    return render(request,'formulario_lista_de_pedido.html')
