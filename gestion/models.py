from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.html import mark_safe
from cloudinary.models import CloudinaryField
#permissionMixin > modulo de permissions
#AbstractBaseUser< me sirve para modificar mi auth_user en su totalidad

# Create your models here.
# class Imagen (models.Model):
#         nombre = models.ImageField()

#         def __str__(self):
#                 #sirvef para indicar como se mostrar la instancia al momento de ser solicitada
#                 return self.nombre
        
#         def nombre_tag(self):
#                 return mark_safe('<img src="/imagenes/%s" width="150" height="150"/>' %(self.nombre))
        
#         #sirvef para indicar el nombre de este "atributo"
#         nombre_tag.short_description= "Figura de la imagen"

#         class Meta:
#                 db_table= "imagenes"

#                 verbose_name_plural="imagenes"

class Categoria(models.Model):
        nombre = models.TextField(unique=True)
        # imagen = models.OneToOneField(to=Imagen, on_delete=models.RESTRICT, db_column="imagen_id")
        imagen= CloudinaryField("categoria")
        class Meta:
                db_table = "categorias"

class Producto (models.Model):
        nombre = models.TextField()
        fechaVencimiento= models.DateField(db_column="fecha_vencimiento")
        lote = models.TextField(null=False)
        precio = models.FloatField(null=False)
        categoria = models.ForeignKey(to= Categoria, on_delete=models.CASCADE, db_column="categoria_id", related_name="productos")
        # imagen = models.OneToOneField(to = Imagen, on_delete=models.RESTRICT, db_column="imagen_id", related_name="producto")
        imagen = CloudinaryField("producto")
        class Meta:
                db_table= "productos"
                #si queremos que vaya de manera ASC no es necesario hacer nada
                # si queremos que vaya de manera DESC se le coloca el '-' al comienzo
                        # primero ordenara los productos alfabeticamente(A-Z)n y luego de manera DESC las fechas vencimiento
                ordering = ["nombre","-fechaVencimiento"]

class ManejoUsuario(BaseUserManager):
        #para poder utilizar los metodos para obterner la data y utilizar el modelo pero para modigficar cierta funcionabilidad
        def create_superuser(self, nombre, apellido, email, password, tipo):
                # metodo que se manda a llamar cuando en la terminal creams un super ususario
                if not email:
                        raise ValueError("El correo es obligatorio")
                #quita caracteres especiales como tildes , mayusculas y otros para que el correo n se guarde de esa manera
                emailNormalizado = self.normalize_email(email)
                nuevoUsuario = self.model(email = email, nombre=nombre, tipo=tipo, apellido=apellido)
                # generar el hash de la contraseña
                # set_password > metodo propio del auth_user que sirve para generar el hash de la contraseña usando los mimos principios que la libreria bcrypt
                nuevoUsuario.set_password(password)

                nuevoUsuario.save()



class Usuario(AbstractBaseUser,PermissionsMixin):
        nombre = models.TextField(null=False)
        apellido = models.TextField(null=False)
        email = models.EmailField(unique=True, null=False)
        password= models.TextField(null=False)
        tipo = models.TextField(choices=[("ADMIN","ADMIN"),("CAJERO","CAJERO")])  #("ADMIN","ADMIN") = ("SEMUESTRA FRONT", "SE MUESTRA EN BACK")
        is_staff= models.BooleanField(default=False)

        # Sirve para indicarle que campo utilizara para encontrar al usuario por el panel administrativo
        USERNAME_FIELD= "email"

        #campos que son requeridos al usar el comando para crear un superusuario en la consola, es indiferente si le colocamos null=False
        REQUIRED_FIELDS= ["apellido","nombre","tipo"]
        
        objects =ManejoUsuario()

        class Meta:
                db_table ="usuarios"

