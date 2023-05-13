class producto:
    #constructor() { ... }
    def __init__(self, nombre, precio, disponibilidad, imagen):
        self.nombre = nombre
        self.precio = precio
        self.disponibilidad =disponibilidad
        self.imagen = imagen
    def mostrar_imagen(self ):
        return self.imagen   

shampoo = producto("shampoo", 7.40, True, "https://google.com")

print(shampoo.mostrar_imagen())