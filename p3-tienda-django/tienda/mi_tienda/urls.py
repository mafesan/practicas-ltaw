from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'product/', views.music_detail),
    url(r'discos/$', views.music_index),
    url(r'libros/$', views.book_index),
    url(r'bicis/$', views.bike_index),
]
