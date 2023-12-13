from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from tiendas.models import Tienda
from productos.models import Producto

def gestion_tiendas(request):
    tiendas = Tienda.objects.all()
    return render(request, 'gestionTienda/gestion_tienda.html', {'tiendas': tiendas})

def gestion_productos(request):
    productos = Producto.objects.all()
    return render(request, 'gestion_productos.html', {'productos': productos})

def tienda_detalle(request, tienda_id):
    tienda = get_object_or_404(Tienda, pk=tienda_id)
    productos = Producto.objects.filter(tienda=tienda)
    return render(request, 'tienda_detalle.html', {'tienda': tienda, 'productos': productos})