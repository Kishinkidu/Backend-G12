from sqlalchemy import Column, types, ForeignKey
from config import conexion


class Publicacion(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    titulo=Column(type_=types.Text, nullable=False)
    descripcion=Column(type_=types.Text, nullable=True)
    habilitado=Column(type_=types.Boolean, default=True)
    usuarioId=Column( ForeignKey(column="usuarios.id"), type_=types.Integer,name="usuario_id", nullable=False )

    __tablename__ ="publicaciones"
