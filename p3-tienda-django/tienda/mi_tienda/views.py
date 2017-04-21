from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .forms import SignUpForm, SearchForm

from .models import Disco, Libro, Bici, Carrito

list_carrito = ()
    
def index(request):
        context = {}
        return render(request, 'mi_tienda/index.html', context)


def ver_todo(request):
    print "paso por ver todo"
    form = SearchForm()
    search = {}
    if request.method == "POST":
        print request.POST
        search = request.POST["search_text"]
        music_autor = Disco.objects.filter(autor__icontains=search)
        music_titulo = Disco.objects.filter(titulo__icontains=search)
        music_list = (music_autor | music_titulo).distinct()

        book_autor = Libro.objects.filter(autor__icontains=search)
        book_titulo = Libro.objects.filter(titulo__icontains=search)
        book_list = (book_autor | book_titulo).distinct()

        bici_marca = Bici.objects.filter(marca__icontains=search)
        bici_modelo = Bici.objects.filter(modelo__icontains=search)
        bici_list = (bici_marca | bici_modelo).distinct()
    else:
        music_list = Disco.objects.order_by('titulo')
        book_list = Libro.objects.order_by('titulo')
        bici_list = Bici.objects.order_by('marca')

    context = {'music_list': music_list, 'book_list': book_list, 'bici_list': bici_list, 'form': form, 'form_result': search}
    return render(request, 'mi_tienda/index-todo.html', context)

def product_detail(request, product_type, field1, field2):
    print "paso por product_detail"
    print request
    if product_type == "discos":
        objeto = Disco.objects.get(autor=field1, titulo=field2)
    elif product_type == "libros":
        objeto = Libro.objects.get(autor=field1, titulo=field2)
    elif product_type == "bicis":
        objeto = Bici.objects.get(marca=field1, modelo=field2)
    else:
        objeto = {}

    context = {'product_data': objeto, 'product_type': product_type}

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
    list_carrito = Carrito.objects.order_by('tipo_producto')
    context = {'list_carrito': list_carrito}
    return render(request, 'mi_tienda/carrito.html', context)

def llenar_carrito(request, product_type, field1, field2):

    print "paso por llenar carrito"
    if product_type == "disco":
        objeto = Disco.objects.get(autor=field1, titulo=field2)
    elif product_type == "libro":
        objeto = Libro.objects.get(autor=field1, titulo=field2)
    elif product_type == "bici":
        objeto = Bici.objects.get(marca=field1, modelo=field2)

    if objeto.cantidad >= 1:
        objeto.cantidad -= 1
        objeto.save()
        nuevo_objeto = Carrito.objects.create(tipo_producto=product_type, campo1=field1, campo2=field2)
        list_carrito = Carrito.objects.order_by('tipo_producto')
        context = {'nuevo_objeto': nuevo_objeto, 'list_carrito': list_carrito}
        return render(request, 'mi_tienda/carrito.html', context)
    else:
        context = {'product_data': product_data, 'product_type': bool_product_data}


def eliminar_carrito(request, product_type, field1, field2):
    print "paso por eliminar carrito"
    #TODO
    Carrito.objects.filter(tipo_producto=product_type, campo1=field1, campo2=field2).delete()
    list_carrito = Carrito.objects.order_by('tipo_producto')

    if product_type == "disco":
        objeto = Disco.objects.get(autor=field1, titulo=field2)
    elif product_type == "libro":
        objeto = Libro.objects.get(autor=field1, titulo=field2)
    elif product_type == "bici":
        objeto = Bici.objects.get(marca=field1, modelo=field2)

    objeto.cantidad += 1
    objeto.save()
    context = {'list_carrito': list_carrito}
    return render(request, 'mi_tienda/carrito.html', context)
