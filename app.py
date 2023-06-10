from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from flask_migrate import Migrate
from config import conexion
from models.usuario_model import Usuario
from models.publicacion_model import Publicacion
from controllers.usuario_controller import RegistroController, PerfilController, LoginController
from flask_jwt_extended import JWTManager
from controllers.publicacion_controller import PublicacionesController,PublicacionController
from datetime import timedelta

from os import environ # muestra las variables de entorno

load_dotenv()
# las variables de entrorno son variable que estan presente de manera GLOBLAL en toda la maquina/ servidor y es aca donde se suelen guardar las credenciales ( a la bd, informacion a otras API´S, mensajeria(email), entre otros), crendeciales sensibles que no deben ser expuestas.
app = Flask (__name__)
api=Api(app)
app.config["JWT_SECRET_KEY"] = environ.get("SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] =timedelta(hours = 1, minutes = 30)
#busca en la vvariable config  la variable JWT_SECRET_KEY > Sera el secreto por el cual se generaran los tokens
jwt = JWTManager(app)

@jwt.unauthorized_loader
def tokenRequerida(razon):
    print(razon)
    
    return{
        "message" : "Se necesita una token para realizar esta accion"
    },401

@jwt.invalid_token_loader
def tokenInvalida(reason):
    print (reason)
    message= ""
    if reason == 'Not enough segments':
        message = 'La token tiene que tener 3 segmentos, el header, payload y signature'
        
    elif reason == "Invalid header string: 'utf-8' codec can't decode byte 0xc7 in position 0: invalid continuation byte":
        message = 'Token invalida'

    elif reason =='Signature verification failed':
        message = 'Esta token no pertenece a esta API'

    return {
        "message ": message
    },401



#el metodo .get de los dicionarios intentara buscar esa llave y si no existe, retornara None, a diferencia de las [] (llaves ) que si no encuentra emitira un error de tipo KeyError.
#el metodo.get() solamente se puede utilizar para devolver o visualizar los valores , mas no para asignar mientras que las llaves[] son para lectura y escritura
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DATABASE_URL")
#app.config["SQLALCHEMY_DATABASE_URI"] = environ["DATABASE_URL"]

conexion.init_app(app)

Migrate(app,conexion)

#declaramos la ruta
api.add_resource(RegistroController,"/registro-usuario")
api.add_resource(LoginController,"/login")
api.add_resource(PerfilController,"/perfil")
api.add_resource(PublicacionesController,"/publicaciones")
api.add_resource(PublicacionController, "/publicacion/<int:id>")
if __name__=="__main__":
    app.run(debug=True)