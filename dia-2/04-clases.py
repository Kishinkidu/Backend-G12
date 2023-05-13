from datetime import datetime

class persona:
    nombre = "juan"
    edad = 28
    correo = "jperez@gmail.com"
    peso = 89.5

    def decir_hora(self):
        hora_actual = datetime.now()
        data= hora_actual.strftime("%I-%p")
        hora, turno = data.split("-")
        # print(hora)
        # print(turno)
        if turno == "pm":
            print("son las {} de la noche".format(hora))
        else:
            print("son las {} de la mañana".format(hora))
    
    def saludar(self):
        print("Hola! Soy {}".format(self.nombre))

#variable pasa a llamarse isntancia (copia de la clase que sera almacenada en esa varuable)
persona1 = persona()
persona1.nombre ="roberto"
persona1.saludar()
print(persona1.nombre)

persona2 = persona()
persona2.decir_hora()
print(persona2.nombre)