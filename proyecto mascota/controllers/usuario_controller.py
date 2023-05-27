from flask_restful import Resource, request
from base_de_datos import conexion
from models.Ususarios_model import UsuarioModel
from dtos.usuario_dto import UsuariosResponseDto, UsuariosRequestDto

class UsuarioController(Resource):
    #cuando yo heredo la clase Resource ahora los metodos que yo cree con el mismo nombre que un metodo HTTP ( GET, POST , PUT , DELETE) entocnes ingresaran a esos metodos
    def get(self):
        resultado = conexion.session.query(UsuarioModel).all()
        #many = True > el dtoo iterara el arreglo o listaa y convertira en cada uno de ellos
        dto=UsuariosResponseDto(many = True)
        # dump > convierte la distancia de la clase en un diccionarios
        data = dto.dump(resultado)
        # data = []
        # for usuario in resultado:
        #     data.append({
        #         "id": usuario.id,
        #         "nombre": usuario.nombre,
        #         "apellido": usuario.apellido,
        #         "correo": usuario.correo,
        #         "dni": usuario.dni
        #     })

        return{
            "content": data
        }
    
    def post(self):
        data = request.json
        dto = UsuariosRequestDto()
        # load > valida el diccionario que le pasamos conlos campos que cumplan las condiciones ( requeridos , que sean del tipo de dato correcto)
        dataValidada = dto.load(data)
        print(dataValidada)
        #Inicializo mi nuevo usuario 
        nuevoUsuario = UsuarioModel(**dataValidada)
        # nuevoUsuario = UsuarioModel(nombre="Erick", apellido="Revoredo", correo="asdasd@fgmail.com", dni= "78563489")
        #indicar que vamos a agregar un nuevo registro
        conexion.session.add((nuevoUsuario))
        try:
            #se usa para transacciones, serve para indicar que todos los cambios se guarder permantente, si no hacemos el comit entonces no de guardara la infromacion de manera permanente
            conexion.session.commit()
            return{
                "message": "Usuario creado exitosamente"
            }, 201 #
        except Exception as error:
            # rollback > para retroceder y dejar todos los posibles cambios sin efecto ( los incrementadores, nuevos registros,actualizaciones y eliminaciones) quedan sin efecto.
            conexion.session.rollback()
            return{
                "message":"Error al crear el usuario",
                "content" : error.args # args > argumentos (porque fallo)
            }, 400 #bad request (mala solicitud por parte del cliente)