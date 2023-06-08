from flask_restful import Resource, request
from models.publicacion_model import Publicacion
from config import conexion
from flask_jwt_extended import get_jwt_identity, jwt_required
from dtos.publicacion_dto import PublicacionRequestDto, PublicacionResponseDto
from models.usuario_model import Usuario

class PublicacionesController(Resource):
    @jwt_required()
    def post(self):
        usuarioId = get_jwt_identity()
        dto = PublicacionRequestDto()

        try:
            dataValidada = dto.load(request.json)
            nuevaPublicacion = Publicacion(**dataValidada, usuarioId=usuarioId)

            conexion.session.add(nuevaPublicacion)
            conexion.session.commit()

            dtoRespuesta = PublicacionResponseDto()
            resultado = dtoRespuesta.dump(nuevaPublicacion)
            return {
                "message": "publicacion creada exitosamente",
                "content": resultado
            }, 201
        except Exception as e:
            conexion.session.rollback()
            return {
                "message": "Error al crear al publicacion",
                "content": e.args
            }, 400

    def get(self):
        queryParams = request.args
        usuarios = conexion.session.query(Usuario).filter_by(**queryParams).all()

        print(usuarios)
        
        resultado = conexion.session.query(Publicacion).all()
        
        dto = PublicacionResponseDto(many = True)
        publicaciones = dto.dump(resultado)
        return {
            "content" : publicaciones
        }