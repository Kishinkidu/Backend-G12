from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.Ususarios_model import UsuarioModel


# DTO > Data Transfer Object ( objeto de transferencia de datos)
class UsuariosResponseDto(SQLAlchemyAutoSchema):
    class Meta:
        #sirve para pasar metadatos (informacion adicional) a la clase de la cual estoy heredando sin la necesidad de modifica directamente o llamar a sus metodos directamente
        model = UsuarioModel
class UsuariosRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        #sirve para pasar metadatos (informacion adicional) a la clase de la cual estoy heredando sin la necesidad de modifica directamente o llamar a sus metodos directamente
        model = UsuarioModel