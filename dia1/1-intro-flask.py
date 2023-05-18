from flask import Flask, request

app = Flask(__name__)

productos = [
    {"id": 1, "nombre": "martillo", "precio": 5.8, "disponible": True},
    {"id": 2, "nombre": "serrucho", "precio": 20.5, "disponible": True},
    {"id": 3, "nombre": "taladro", "precio": 120.0, "disponible": True},
]


@app.route("/productos", methods=["GET", "POST"])
def gestionProductos():
    # request , me da toda la informacion del cliente
    print(request.method)
    if request.method == "GET":
        return {"message": "los productos son", "content": productos}
    elif request.method == "POST":
        print(request.json)
        id = len(productos) + 1
        data = request.json
        data["id"] = id
        # crea una nueva data llamada id si no existe.
        productos.append(data)
        return {"message": "producto creado exitosamente"}


@app.route("/producto/<int:id>", methods=["GET"])
def gestionProducto(id):
    if request.method == "GET":
      resultado = None
    for producto in productos:
        if producto["id"] == "id":
            resultado = producto
            break
        if resultado is None:
            return {"message": " no se encontro el producto a buscar"}
        else:
            return {"message": " el producto es", "content":resultado}
    
      

if __name__ == "__main__":
    app.run(debug=True)
