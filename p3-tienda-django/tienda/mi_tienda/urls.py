from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'tienda/$', views.index),
    url(r'discos/$', views.music_index),
    url(r'libros/$', views.book_index),
    url(r'bicis/$', views.bike_index),
    url(r'product/(?P<product_type>\w+)/(?P<field1>\w+)/(?P<field2>\w+)', views.product_detail),
]
