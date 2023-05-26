from sqlalchemy import Column, ForeignKey
from sqlalchemy import types
from base_de_datos import conexion
from enum import Enum


class SexoEnum(Enum):
    Macho ="Macho"
    Hembra = "Hembra"
    Otros = "Otros"

class MascotaModel(conexion.Model):
    id = Column(autoincrement=True, type_= types.Integer, primary_key=True)
    nombre=Column(type_=types.Text, nullable=False)
    apellido=Column(type_=types.Text, nullable=True)
    sexo=Column(type_=types.Enum(SexoEnum), default= SexoEnum.Otros)
    #name> para indicar como queremos que se llame esta columna en la base de datos, sin no le pones este parametro su nombre sera igual quel el nombre del atributo
    fecha_de_nacimiento=Column(type_=types.Date, name="fecha_nacimiento")
    raza=Column(type_=types.Text, default="otro")
    #realacion nuestra tabla usuarios con mascotas
    usuarioId= Column (ForeignKey(column="usuarios.id"), type_=types.Integer, nullable=False, name="usuario_id")

    __tablename__="mascotas"