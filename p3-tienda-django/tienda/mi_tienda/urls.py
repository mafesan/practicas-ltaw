from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'tienda/$', views.index),
    url(r'todo/$', views.ver_todo),
    url(r'discos/$', views.music_index),
    url(r'libros/$', views.book_index),
    url(r'bicis/$', views.bike_index),
    url(r'carrito/$', views.carrito),
    url(r'comprar/(?P<product_type>\w+)/(?P<field1>[\w ]+)/(?P<field2>[\w ]+)', views.llenar_carrito),
    url(r'product/(?P<product_type>\w+)/(?P<field1>[\w ]+)/(?P<field2>[\w ]+)', views.product_detail),
]
