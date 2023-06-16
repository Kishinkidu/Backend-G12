from django.db import models

# Create your models here.


class Categoria(models.Model):
    # el id se puede crear o no crear( es obligatorio a nivel de bd) pero si no lo declaramos DJANGO igual creara el bd
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(null=False, unique=True)
    estante = models.TextField()
    piso = models.TextField()
    habilitado = models.BooleanField(default=True)

    class Meta:
        # https://docs.djangoproject.com/en/4.2/ref/models/options/
        # Sirve para pasar metadata o informacion a la clase de la cual estamos heredando
        db_table = "categoria"
        # estante     piso
        #    A          1
        #    A          2 (OK)
        #    B          1  (OK)
        #    A          1  (ERROR)
        unique_together = ["estante", "piso"]


class Libro(models.Model):
    # no coloca el ID por que django lo creara automaticamente
    titulo = models.TextField(null=False)
    fechaPublicacion = models.DateTimeField(db_column="fecha publicacion")
    unidades = models.IntegerField(default=0)
    sinopsis = models.TextField()
    # on_delete > sirve para indicar que va a suceder cuando se intente eliminar una categoria
    # CASCADE > elminara la categoria y luego todos sus libros
    # SET_NULL > eliminara la categoria y a los libros les cambiara el valor a NULL en la bd
    # SET_DEFAULT > eliminara la categoria y cambiara el valor a un valor por defecto colocado en el parametro DEFAULT
    # DO_NOTHING > elimina la categoria y no cambia el valor de la categoria a la cual pertenece el libro, NO SE RECOMIENDA UTILIZAR ESTO porque genera mala integracio de datos
    categoria = models.ForeignKey(
        to=Categoria, db_column="categoria_id", related_name="libros", on_delete=models.CASCADE)

    class Meta:
        db_table = "libros"


class Autor(models.Model):
    # nombre tiene que  not null
    # nacionalidad tiene que se tex
    # foto imagefield
    # el nombre y nacionalidad nos e puede repetir
    nombre = models.TextField(null=False)
    nacionalidad = models.TextField()
    foto = models.ImageField()
    # se crea una realacion de muchos a muchos y esto creara la tabla puente, pivote o detalle
    # https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_many/
    libros = models.ManyToManyField(to=Libro)

    class Meta:
        db_table = "autores"
        unique_together = ["nombre", "nacionalidad"]

# si no utilizacemos la clase ManytoManyField tendriamos que hacerlo manualmente
