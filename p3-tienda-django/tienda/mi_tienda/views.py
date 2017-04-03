from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Disco, Libro, Bici

def index(request):
    latest_music_list = Disco.objects.order_by('fecha_pub')
    latest_book_list = Libro.objects.order_by('fecha_pub')
    latest_bici_list = Bici.objects.order_by('marca')
    context = {'latest_music_list': latest_music_list, 'latest_book_list': latest_book_list, 'latest_bici_list': latest_bici_list}
    return render(request, 'mi_tienda/index.html', context)

def music_detail(request):
    response = '<html><head><title>Bad</title></head><body>Ups!</body></html>'
    return HttpResponse(response)
