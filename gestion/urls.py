from django.urls import path
from .views import saludar, CategoriasController, CategoriaController,alternarEstadoCategoria

urlpatterns = [
    path("",saludar),
    #as_view > convierte la clase en una vista que djanfo pueda enternder  recordemos que Django trabaja con HTML'S, en otras palabras con vistas)
    path("categorias", CategoriasController.as_view()),
    path("categoria/<int:id>", CategoriaController.as_view()),
    path("toggle-categoria/<int:id>", alternarEstadoCategoria)
]