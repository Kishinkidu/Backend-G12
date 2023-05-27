from models.mascota_model import MascotaModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class MascotaRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = MascotaModel
        #indicamos al DTO que tambien haga avalidacion en las columnas que tienen llaves foraneas
        include_fk =True