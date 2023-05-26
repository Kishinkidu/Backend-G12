from sqlalchemy.schema import Column
from sqlalchemy import types
from base_de_datos import conexion 

class UsuarioModel(conexion.Model):
    # https://docs.sqlalchemy.org/en/20/core/type_basics.html#module-sqlalchemy.types
    # https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.Column
    id = Column(type_= types.Integer,autoincrement=True,primary_key=True)
    nombre = Column(type_=types.Text, nullable=False)
    apellido = Column(type_= types.Text)
    correo = Column(type_= types.Text, unique=True, nullable=True)
    dni = Column(type_=types.Text, unique=True ,nullable=True)

# como se llamara la tabla en la base de datos , sii no le ponemos este nombre sera el mismo que la clase(ususario)
    __tablename__ ="usuarios"