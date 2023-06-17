from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from django.http  import HttpRequest
from rest_framework.views import APIView
from .selializers import CategoriaSerializer, LibroSerializer, AutorSerializer, LibroAutorSerializer, AutorConLibrosSerializer
from .models import Categoria, Libro, Autor
from rest_framework import status

@api_view(["GET", "POST"])
def saludar(request: Request | HttpRequest):
    print(request.method)
    return Response(data={
        "message":"Bienvenido a mi API de librerias"
    })

class CategoriasController(APIView):
    #es exactamente iguar que la clase Resource de flask restful
    def get( self,request):
        #SELECT * FROM categorias WHERE habilitado = True
        categorias = Categoria.objects.filter(habilitado = True).all()
        print (categorias)

        #serializador para convertirlas a un diccionario
        resultado = CategoriaSerializer(instance=categorias, many=True)
        return Response(data={
            "message" : "Las categorias son",
            "content": resultado.data #data > encargado de devolver el diccionario
        })
    
    def post( self, request: Request | HttpRequest):
        # vamos a crear un dto > pasa a llamarse serializador
        serializer = CategoriaSerializer
        data = request.data
        serializador = CategoriaSerializer(data=data)
        try:
            serializador.is_valid(raise_exception=True)
            # si la validacion pasa exitosamente entonces se agregar a la instancia del serializador el atributo validated_data en la cual se almacenara nuestra informacion validada(corroborada)
            print(serializador.validated_data)
            categoriaCreada= serializador.save()
            print(categoriaCreada)
            respuesta = CategoriaSerializer(instance=categoriaCreada)
            return Response(data={
                "message": "Categoria creada exitosamente",
                "content": respuesta.data # data > atributo que convierte la instancia a un diccionario utilizando tipos de datos complejos
            })
        except Exception as err:
            return Response(data={
                "message": "Error al crear la categoria",
                "content": err.args
            })

class CategoriaController (APIView):
    def  get(self, request: Request | HttpRequest, id:int):
        print(id)
        #solamente mostrar si la categoria esta habilitada
        # SELECT *FROM categorias WHERE id = "..." AND habilitado = True;
        categoriaEncontrada = Categoria.objects.filter(id = id, habilitado = True).first()

        if not categoriaEncontrada:
            return Response(data={
                "message":"Categoria no existe"
            })
        serializador = CategoriaSerializer(instance=categoriaEncontrada)
        return Response(data = {
            "content":serializador.data
        })
    
    def put(self, request: Request| HttpRequest, id: int):
        categoriaEncontrada = Categoria.objects.filter(id = id).first()

        if not categoriaEncontrada:
            return Response(data ={
                "message":"Categoria no existe"
            })
        
        serialiador = CategoriaSerializer(data = request.data)
        try:
            serialiador.is_valid(raise_exception=True)
            dataValidada = serialiador.validated_data

            # metodo proveniente del serializer que actualiza la informacion de la categoria
            serialiador.update(instance=categoriaEncontrada, validated_data=dataValidada)

            return Response(data={
                "message":"Categoria actualizada exitosamente",
                "content": serialiador.data
            })
        except Exception as err:
            return Response (data= {
                "message": "Error al actualizar categoria",
                "content": err.args
            }, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request: Request|HttpRequest, id : int):
        categoriaEncontrada = Categoria.objects.filter(id=id).first()
        if not categoriaEncontrada:
            return Response(data={
            "message": "categoria no existe"
            })
        resultado = Categoria.objects.filter(id=id).delete()
        print(resultado)

        return Response(data=None, status= status.HTTP_204_NO_CONTENT)
    

@api_view(["POST"])
def alternarEstadoCategoria(request, id):
    categoriaEncontrada = Categoria.objects.filter(id=id).first()

    if not categoriaEncontrada:
        return Response(data ={
            "message" : "Categoria no existe"
        })
    
    categoriaEncontrada.habilitado = not categoriaEncontrada.habilitado

    #sobreescribe la infromacion cambiada
    categoriaEncontrada.save()
    #RESULTADO_VERDADERO if CONDICION else RESULTADO_FALSO
    message = "habilitado" if categoriaEncontrada.habilitado == True else "deshabilitado"

    return Response(data ={
        "message" : "Categoria "+message+" correctamente"
    })


class librosController(APIView):
    def post(self, request: Request|HttpRequest):
        serializador = LibroSerializer(data = request.data)
        validado = serializador.is_valid()
        if validado:
            serializador.save()
            return Response(data={
                "message":"Libro creado exitosamente"
            }, status= status.HTTP_201_CREATED)
        else:
            return Response(data={
                "message":"Error al crear el libro",
                "content" : serializador.errors
            },status = status.HTTP_400_BAD_REQUEST)
    def get(self,request:Request|HttpRequest):
        print(request.query_params)
        # https://docs.djangoproject.com/en/4.2/topics/db/queries/#field-lookups
        # contains > hace match con palabras sensibles a mayusculas
        # icontains > no respeta mays ni minus
        parametros = {}
        if request.query_params.get("titulo"):
            parametros["titulo__icontains"]=request.query_params.get("titulo")

        if request.query_params.get("anio"):
            parametros["fechaPublicacion__year"]=request.query_params.get("anio")

        libros =Libro.objects.filter(**parametros).all()
 
        resultado = LibroSerializer(instance=libros, many = True)
        return Response(data = {
            "content": resultado.data
        })
    
class AutoresController(APIView):
    def post (self, request: Request|HttpRequest):
        serializador= AutorSerializer(data= request.data)
        try:
            serializador.is_valid(raise_exception=True)
            serializador.save()

            return Response(data={
                "message":"Autor creado exitosamente"
            },status= status.HTTP_201_CREATED)
        
        except Exception as err:
            return Response(data = {
                "message":"Error al crear el autor",
                "content": err.args
            },status= status.HTTP_400_BAD_REQUEST)
        
    def get(self, request:Request|HttpRequest):
        autores = Autor.objects.all()
        serializador = AutorSerializer(instance=autores, many= True)

        return Response(data={
            "content": serializador.data
        })
    
class AutoresLibrosController(APIView):
    def post(self, request:Request|HttpRequest):
        return Response(data={
            "message":"Autor vinculado con el libro exitosamente"
        })
    
class LibroAutoresController(APIView):
    def post(self,request:Request|HttpRequest):
        serializador = LibroAutorSerializer(data = request.data)
        try:
            serializador.is_valid(raise_exception=True)
            dataValidada = serializador.validated_data
            autorId= dataValidada.get("autorId")
            libroId= dataValidada.get("libroId")
            libro = Libro.objects.filter(id=libroId).first()
            if not Libro:
                raise Exception('Libro no existe')
            autor= Autor.objects.filter(id=autorId).first()
            if not Autor:
                raise Exception('autor no existe')
            
            autor.libros.add(libro)
            autor.save()

            return Response (data = {
                "message": "autor vinculado con el libro exitosamente"
            }, status = status.HTTP_201_CREATED)
        
        except Exception as err:
            return Response(data={
                "message":"Error al crear el libro con el autor",
                "content": err.args
            }, status= status.HTTP_400_BAD_REQUEST)
        
@api_view(["GET"])
def mostrarInforAutor(request:Request|HttpRequest, id:int):
    autor = Autor.objects.filter(id=id).first()
    if not autor:
        return Response(data={
            "message":"Autor no existe"
        }, status=status.HTTP_400_BAD_REQUEST)
    serializador = AutorConLibrosSerializer(instance=autor)
    # cuando yo uso el atributo libros se hace un inner join entre la tabla autores y la tabla autores_libro
    print(autor.libros.all())
    return Response(data={
        "content": serializador.data
    })