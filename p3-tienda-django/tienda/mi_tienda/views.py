from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Disco, Libro, Bici, Carrito

list_carrito = ()
def index(request):
    context = {}
    return render(request, 'mi_tienda/index.html', context)


def ver_todo(request):
    print "paso por ver todo"
    latest_music_list = Disco.objects.order_by('titulo')
    latest_book_list = Libro.objects.order_by('titulo')
    latest_bici_list = Bici.objects.order_by('marca')
    context = {'latest_music_list': latest_music_list, 'latest_book_list': latest_book_list, 'latest_bici_list': latest_bici_list}
    return render(request, 'mi_tienda/ver-todo.html', context)

def product_detail(request, product_type, field1, field2):
    print "paso por product_detail"
    print request
    output = product_type + "," + field1 + ", " + field2

    if product_type == 'discos':
        all_products = Disco.objects.order_by('titulo')
    elif (product_type == 'libros'):
        all_products = Libro.objects.order_by('titulo')
    else:
        all_products = Bici.objects.order_by('modelo')

    product_data = {}
    bool_product_data = {'is_libro': False, 'is_disco': False, 'is_bici': False}
    if product_type == 'discos':
        bool_product_data['is_disco'] = True
        for product in all_products:
            if (product.autor == field1) and (product.titulo == field2):
                product_data = product
    elif product_type == 'libros':
        bool_product_data['is_libro'] = True
        for product in all_products:
            if (product.autor == field1) and (product.titulo == field2):
                product_data = product
    elif product_type == 'bicis':
        bool_product_data['is_bici'] = True
        for product in all_products:
            if (product.marca == field1) and (product.modelo == field2):
                product_data = product

    context = {'product_data': product_data, 'product_type': bool_product_data}

    return render(request, 'mi_tienda/producto.html', context)


def music_index(request):
    print "paso por music_index"
    latest_music_list = Disco.objects.order_by('titulo')
    context = {'latest_music_list': latest_music_list}
    return render(request, 'mi_tienda/index_discos.html', context)

def book_index(request):
    print "paso por book_index"
    latest_book_list = Libro.objects.order_by('titulo')
    context = {'latest_book_list': latest_book_list}
    return render(request, 'mi_tienda/index_libros.html', context)

def bike_index(request):
    print "paso por bike_index"
    latest_bici_list = Bici.objects.order_by('modelo')
    context = {'latest_bici_list': latest_bici_list}
    return render(request, 'mi_tienda/index_bicis.html', context)

def carrito(request):
    print "paso por carrito"
    context = {}
    return render(request, 'mi_tienda/carrito.html', context)

def llenar_carrito(request, product_type, field1, field2):
    print "paso por llenar carrito"
    nuevo_objeto = Carrito.objects.create(tipo_producto=product_type, campo1=field1, campo2=field2)
    list_carrito = Carrito.objects.order_by('tipo_producto')
    context = {list_carrito}
    return render(request, 'mi_tienda/carrito.html', context)
