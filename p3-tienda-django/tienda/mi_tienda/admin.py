from django.contrib import admin

# Register your models here.
from .models import Libro, Disco, Bici, Carrito

class LibroAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Info basica', {'fields': ['titulo', 'autor', 'precio', 'imagen', 'cantidad']}),
        ('Info adicional', {'fields': ['editorial', 'genero', 'fecha_pub']}),
    ]

admin.site.register(Libro, LibroAdmin)
admin.site.register(Disco)
admin.site.register(Bici)
admin.site.register(Carrito)
