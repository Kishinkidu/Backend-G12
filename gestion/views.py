from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request, HttpRequest
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import (AllowAny,  # cualquiera puede usarlo
                                        IsAuthenticated,  # valida que este la token presente y que sea valida
                                        # sera lo mismo que el anterior PERO si es metodo GET no pedira autenticacion
                                        IsAuthenticatedOrReadOnly,
                                        IsAdminUser  # Verificara si el usuario es is_superuser =True
                                        )
from .models import *
from .serializer import *
from cloudinary import uploader



class RegistroUsuarioController(APIView):

    @swagger_auto_schema(request_body=RegistroUsuarioSerializer, operation_description="Regisro de un usuario", operation_summary="Endpoint para registrar usuario")
    def post(self, request: Request | HttpRequest):
        serializador = RegistroUsuarioSerializer(data=request.data)
        try:
            serializador.is_valid(raise_exception=True)
            nuevoUsuario = Usuario(**serializador.validated_data)

            # generar el hash de la password
            password = serializador.validated_data.get("password")
            nuevoUsuario.set_password(password)

            nuevoUsuario.save()

            return Response(data={
                "message": "Usuario creado exitosamente"
            }, status=status.HTTP_201_CREATED)

        except Exception as err:
            return Response(data={
                "message": "Error al crear el ususario",
                "content": err.args
            }, status=status.HTTP_400_BAD_REQUEST)


class CategoriasController(APIView):
    # GET | OPTIONS no pedira la token
    permission_classes = [IsAuthenticatedOrReadOnly,]

    @swagger_auto_schema(request_body=CategoriaSerializer, operation_summary="Crear una categoria")
    def post(self, request: Request | HttpRequest):
        serializador = CategoriaSerializer(data=request.data)
        try:
            serializador.is_valid(raise_exception=True)
            serializador.save()
            return Response(data={
                "message": "Categoria creada exitosamente"
            }, status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response(data={
                "message": "Error al crear Categoria",
                "content": err.args
            }, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={status.HTTP_200_OK: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'content': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_OBJECT, properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER, default=0),
                    'nombre': openapi.Schema(type=openapi.TYPE_STRING),
                    'imagen': openapi.Schema(type=openapi.TYPE_INTEGER), })
            )
        }
    )})
    def get(self, request: Request | HttpRequest):
        categorias = Categoria.objects.all()
        serializador = CategoriaSerializer(instance=categorias, many=True)

        return Response(data={
            "content": serializador.data
        })

class ProdutosController(APIView):
    #se usa cunado los FLIE son ligeros( 1mb maximo)
    parser_classes=[MultiPartParser, FormParser]
    permission_classes = [IsAuthenticatedOrReadOnly,]
    @swagger_auto_schema(request_body=ProductoSerializer, operation_summary="Crear producto")
    def post(self, request:Request|HttpRequest):
        serializador= ProductoSerializer(data=request.data)
        try:
            serializador.is_valid(raise_exception=True)
            serializador.save()
            print(request.data)
            return Response(data={
                "message":"Producto creado exitosamente"
            }, status= status.HTTP_201_CREATED)
        except Exception as err:
            return Response( data={
                "message":"Error al crear Productos",
                "content": err.args
            }, status =status.HTTP_400_BAD_REQUEST)
        
    @swagger_auto_schema(responses={
        status.HTTP_200_OK: openapi.Schema(
        type= openapi.TYPE_OBJECT,
        properties={
            "content": openapi.Schema(
        type=openapi.TYPE_ARRAY,
        items=openapi.Items(type=openapi.TYPE_OBJECT, PROPERTIES={
            "id": openapi.Schema(type=openapi.TYPE_INTEGER, default=0),
            "nombre": openapi.Schema(type=openapi.TYPE_STRING),
            "fechaVencimiento": openapi.Schema(type=openapi.TYPE_STRING),
            "lote": openapi.Schema(type=openapi.TYPE_STRING),
            "precio": openapi.Schema(type=openapi.TYPE_NUMBER),
            "categoria": openapi.Schema(type=openapi.TYPE_INTEGER),
            "imagen": openapi.Schema(type=openapi.TYPE_STRING)
        })
            )
        }
        )
    })
    def get (self,request:Request|HttpRequest):
        productos= Producto.objects.all()
        serializer=ProductoSerializer(instance=productos, many=True)
        return Response(data={
                "content": serializer.data
                },status=status.HTTP_200_OK)
    
class ProductosSegundoMetodoController(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    @swagger_auto_schema(request_body=ProductoSegundoMetodoSerializer, operation_summary="Registrar producto")
    
    def post(self, request:Request|HttpRequest):
        serializador= ProductoSegundoMetodoSerializer(data= request.data)
        try:
            serializador.is_valid(raise_exception=True)
            serializador.save()
            return Response(data={
                "message":"Producto creado exitosamente"
            }, status= status.HTTP_200_OK)
        except Exception as err:
            return Response( data={
                "message":"Error al crear Productos",
                "content": err.args
            }, status =status.HTTP_400_BAD_REQUEST)


class UploadImageController(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    parser_classes=[MultiPartParser, FormParser]
    @swagger_auto_schema(request_body=UploadImageSerializer, operation_summary="Subir imagen")
    def post(self, request:Request|HttpRequest):
        try:
            imagen= request.FILES.get("imagen")
            response=uploader.upload(imagen)
            url= f"v{response['version']}/{response['public_id']}.{response['format']}"
            return Response (data={
                "content": url
            }, status= status.HTTP_201_CREATED)
        except Exception as err:
            return Response(data={
                "message": "Error al crear el producto",
                "content": err.args
            }, status= status.HTTP_400_BAD_REQUEST)