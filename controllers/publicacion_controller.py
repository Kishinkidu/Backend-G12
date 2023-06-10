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
        #solamente necesito el ID
        #with_entities > especificar que colimnnas queremos extraer 
        #con el uso de with_entitties
        #SELECT id,nombre  FROM Usuarios
        data = conexion.session.query(Usuario) .with_entities(Usuario.id).filter_by(**queryParams).all()

        usuariosIds = []
        for id in data:
            usuariosIds.append(id[0])
        
        #data= { "nombre ":"juan"}
        #data.k

        #SELECT * FROM publicaciones WHERE usuariosId = ...
        #SELECT * FROM publicaciones WHERE usuario_id IN (1,2);
        # https://www.postgresql.org/docs/current/functions-subquery.html#FUNCTIONS-SUBQUERY-IN

        resultado = conexion.session.query(Publicacion).filter(Publicacion.usuarioId.in_(usuariosIds)).all()
        
        dto = PublicacionResponseDto(many = True)
        publicaciones = dto.dump(resultado)
        return {
            "content" : publicaciones
        }
    
class PublicacionController(Resource):
    #jwt se encarga de 1. Validar que la token sea nuestra(concuerda el secreto),2. De que la token aun no expiro,3. sea valida
    @jwt_required()
    #/publicacion/<int:id>
    def put(self, id):
        try:
            usuarioId =get_jwt_identity()

            publicacion = conexion.session.query(Publicacion).filter_by(id = id, usuarioId = usuarioId).first()
            #ublicacion = conexion.session.query(Publicacion).filter(Publicacion.id == id, Publicacion.usuarioId == usuarioId).first()
            if not publicacion:
                raise Exception("Publicacion no existe")
            dto= PublicacionRequestDto()
            dataValidada = dto.load(request.json)
            #Primera forma
            # publicacion.titulo = dataValidada.get("titulo")
            # publicacion.descripcion = dataValidada.get("descripcion")
            # publicacion.habilitado = dataValidada.get("habilitado")


            #segunda forma
            conexion.session.query(Publicacion).filter_by(id = id, usuarioId=usuarioId).update(dataValidada)

            #Para guardar los cambios
            conexion.session.commit()
            resultado = PublicacionResponseDto().dump(publicacion)

            return{
                    "message" :"Publicacion actualizada exitosamente",
                    "content" : resultado
            }, 201
        except Exception as e:
            return{
                "message":"error al intentar actualizar",
                "content": e.args
            }, 400
        
    @jwt_required()

    def delete(self,id):
        try:
            usuarioId = get_jwt_identity()
            publicacionesEliminadas= conexion.session.query(Publicacion).filter_by(id=id, usuarioId=usuarioId).delete()

            if publicacionesEliminadas == 0:
                raise Exception("No se encontro la publicacion a eliminar")
            conexion.session.commit()

            #segunda forma
            # publicacionEncontrada = conexion.session.query(Publicacion).filter_by(id=id, usuarioId=usuarioId).first()

            # if not publicacionEncontrada:
            #     raise Exception("no se encontro la publicacion a eliminar")
            # conexion.session.delete(publicacionEncontrada)
            # conexion.session.commit()
            return{
                "message":"Publicacion eliminada exitosamente"
            },201
        except Exception as e:
            return{
                "message":"Error al eliminar la publicacion",
                "content": e.args
            },400