from sqlalchemy import Column, types, ForeignKey
from config import conexion
from usuario_model import Usuario

class Publicacion(conexion.Moldel):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    titulo=Column(type_=types.Text, nullable=False)
    descripcion=Column(type_=types.Text, nullable=True)
    habilitado=Column(type_=types.Boolean, default=True)
    usuarioId=Column( ForeignKey(column="Usuario.id"), type_=types.Integer,name="usuario_id", nullable=False )

    __tablename__ ="Publicacion"
