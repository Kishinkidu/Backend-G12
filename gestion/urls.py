from django.urls import path
from .views import saludar, CategoriasController, CategoriaController,alternarEstadoCategoria, librosController, AutoresController,LibroAutoresController,mostrarInforAutor
#me sirve para indicar unn conjunto de rutas estaticas (mostrar gfeneralmente archivos)
from django.conf.urls.static import static
# sirve para obtener los vfalores de las variables seteadas en el archivo setting.py
from django.conf import settings
urlpatterns = [
    path("",saludar),
    #as_view > convierte la clase en una vista que djanfo pueda enternder  recordemos que Django trabaja con HTML'S, en otras palabras con vistas)
    path("categorias", CategoriasController.as_view()),
    path("categoria/<int:id>", CategoriaController.as_view()),
    path("toggle-categoria/<int:id>", alternarEstadoCategoria),
    path("libros", librosController.as_view()),
    path("autores", AutoresController.as_view()),
    path("libros-autores", LibroAutoresController.as_view()),
    path("autor/<int:id>", mostrarInforAutor),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#agrego todos los archivos en la carpeta "imagenes" y con 