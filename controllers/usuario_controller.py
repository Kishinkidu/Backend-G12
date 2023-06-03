from flask_restful import Resource , request
from models.usuario_model import Usuario
from config import conexion
from dtos.usuario_dto import RegistroUsuarioRequestDto, LoginUsuarioRequestDto
from bcrypt import gensalt, hashpw

class RegistroController(Resource):
    def post(self):
        data = request.json
        dto=RegistroUsuarioRequestDto()
        try:
            dataValidada = dto.load(data)
            password = bytes(dataValidada.get("password"), "utf-8")
            #salt > es un texto creado aleatoriamente que se convinara con el password y con ello saldra el hash del passowrd
            salt = gensalt()
            # hashpw> mezcla la password con el salt generado para darnos els hash de la contraseña
            hash = hashpw(password, salt)
            hashString= hash.decode("utf-8")
            print(hashString)
            #Sobreescribimos en el diccionario dataValidada la nueva contraseña hasheada

            dataValidada["password"] = hashString

            nuevoUsuario = Usuario(**dataValidada)
            conexion.session.add(nuevoUsuario)
            conexion.session.commit()

            return{
            "message":"Usuario creado exitosamente"
            }, 201 #creacion
        except Exception as e:
            conexion.session.rollback()
            return{
                "message" : "Error al crear el usuario",
                "content" : e.args
            }, 400 # mala solicitud
        
class LoginController(Resource):
    def post(self):
        dto = LoginUsuarioRequestDto()
        data = request.json
        try:
            dto.load(data)
            return{
                "message" : "Bienvenido"
            }
        except Exception as e: 
            return{
                "message": "Error al hacer el login",
                "content" : e.args
            },400