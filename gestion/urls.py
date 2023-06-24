from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import *

urlpatterns=[
    path ("login", TokenObtainPairView.as_view()),
    path ("registro", RegistroUsuarioController.as_view()),
    path("categorias",CategoriasController.as_view()),
    path("Productos",ProdutosController.as_view()),
    path("Productos-segundo-metodo",ProductosSegundoMetodoController.as_view()),
    path("Upload-image",UploadImageController.as_view()),

    
]