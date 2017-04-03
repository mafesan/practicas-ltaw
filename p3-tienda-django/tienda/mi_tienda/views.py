from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Disco, Libro, Bici

def index(request):
    print "paso por index"
    latest_music_list = Disco.objects.order_by('fecha_pub')
    latest_book_list = Libro.objects.order_by('fecha_pub')
    latest_bici_list = Bici.objects.order_by('marca')
    context = {'latest_music_list': latest_music_list, 'latest_book_list': latest_book_list, 'latest_bici_list': latest_bici_list}
    return render(request, 'mi_tienda/index.html', context)

def product_detail(request, product_type, field1, field2):
    print request
    output = product_type + "," + field1 + ", " + field2

    if product_type == 'discos':
        all_products = Disco.objects.order_by('titulo')
    elif (product_type == 'libros'):
        all_products = Libro.objects.order_by('titulo')
    else:
        all_products = Bici.objects.order_by('modelo')

    product_data = {}
    if product_type == 'discos':
        for product in all_products:
            if (product.autor == field1) and (product.titulo == field2):
                product_data = product
                """product_data['titulo_guiones': product.titulo.replace(' ', '_')]
                product_data['autor_guiones': product.autor.replace(' ', '_')]"""
    context = {'product_data': product_data}

    return render(request, 'mi_tienda/producto.html', context)


def music_index(request):
    print "paso por music_index"
    latest_music_list = Disco.objects.order_by('titulo')
    context = {'latest_music_list': latest_music_list}
    return render(request, 'mi_tienda/index_discos.html', context)

def book_index(request):
    print "paso por book_index"
    context = {}
    return render(request, 'mi_tienda/index_libros.html', context)

def bike_index(request):
    print "paso por bike_index"
    context = {}
    return render(request, 'mi_tienda/index_bicis.html', context)
