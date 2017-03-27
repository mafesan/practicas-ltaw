from django.contrib import admin

# Register your models here.
from .models import Libro, Disco, Bici

class LibroAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Info basica', {'fields': ['titulo', 'autor', 'precio']}),
        ('Info adicional', {'fields': ['editorial', 'genero', 'fecha_pub']}),
    ]

admin.site.register(Libro, LibroAdmin)
admin.site.register(Disco)
admin.site.register(Bici)
