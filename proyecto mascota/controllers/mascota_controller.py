from flask_restful import Resource, request
from base_de_datos import conexion
from models.mascota_model import MascotaModel
from dtos.mascotas_dto import MascotaRequestDto

class MascotasController(Resource):
    def post (self):
        data = request.json
        try:
            dto= MascotaRequestDto()
            dataValidada = dto.load(data)
            nuevaMascota = MascotaModel(**dataValidada)

            conexion.session.add(nuevaMascota)
            conexion.session.commit()

            return {
                    "message" : " mascota creada exitosamente"
            }, 201
        
        except Exception as error:
            conexion.session.rollback()
            return{
                "message":"Error al crear la mascota",
                "content" : error.args
            }