from django.contrib import admin
from .models import( #Imagen,
                        Categoria,Producto,Usuario)

# class ImagenAdmin(admin.ModelAdmin):
#     #clase para agregar algunos filtros al panel adminsitrativo
#     # https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
#     list_display=["id","nombre","nombre_tag"]
#     #modiffica el ordenamiento predeterminado
#     ordering=["-id"]
#     #sirve para indica que se muestren los campos que no son editables
#     readonly_fields=["id", "nombre_tag"]
#     #habilirta un input de busqueda indicando que columnas tiene que buscar
#     # = < que respete mayuscula y minuscula
#     #@ > que haga la busqueda( es como si no le puesiesemos nada)
#     #nada> que no respete mayus ni minus
#     search_fields=["=nombre"]

# para poder visualizar el modelo en el panel administrativo
# admin.site.register(Imagen,ImagenAdmin)
