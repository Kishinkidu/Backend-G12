from flask import Flask
from base_de_datos import conexion
from flask_migrate import Migrate
from models.Ususarios_model import UsuarioModel
from models.mascota_model import MascotaModel
from flask_restful import Api
from controllers.usuario_controller import UsuarioController         
from controllers.mascota_controller import MascotasController

app = Flask(__name__)
#estaremos agregand la libreria flask restful a nuestro proyeecto de falsk
api = Api(app=app)

# dialecto:// username:password@host:port/db name
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost:5432/mascotas"
conexion.init_app(app)

#utilizamos la variable de conexion a la base de datos para setearla en nuestra conexion de sql alchemy
Migrate(app, conexion)

# definir las rutas utilzando la clase Api
api.add_resource(UsuarioController,"/usuarios", "/otra_ruta_usuarios")
api.add_resource(MascotasController, "/mascotas")
if __name__ =="__main__":
    app.run(debug=True)