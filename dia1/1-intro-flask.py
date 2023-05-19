from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app, origins=["http://localhost:5500","http://127.0.0.1:5500"], methods=["GET","PUT","POST","DELETE"])

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
        print(productos)
        return {"message": "los productos son", "content": productos}
    elif request.method == "POST":
        print(request.json)
        id = len(productos) + 1
        data = request.json
        data["id"] = id
        # crea una nueva data llamada id si no existe.
        productos.append(data)
        return {"message": "producto creado exitosamente"}


@app.route("/producto/<int:id>", methods=["GET", "PUT", "DELETE"])
def gestionProducto(id):
    resultado = None
    for producto in productos:
        if producto is None:
            continue
        if producto["id"] == id:
            resultado = producto
            break
    if resultado is None:
        return {"message": " no se encontro el producto a buscar"}

    if request.method == "GET":
        productos_existentes=[]
        for producto in productos:
            if producto is None:
               #evita que el codifgo de acontinuacion no se ejecute por este ciclo
                continue
            productos_existentes.append(producto)
        return {"message": " el producto es", "content": resultado,
                "content": productos_existentes}

    elif request.method == "PUT":
        data = request.json
        productos[id - 1] = data
        # el primer corchete indicara la posicion de la lista y el segundo corchete indicara la propiedad del diccionario
        productos[id - 1]["id"] = id
        return {"message": "actualizado exitosamente"}

    elif request.method == "DELETE":
        productos[id - 1] = None
        return {"message": "producto elminado exitosamente"}


if __name__ == "__main__":
    app.run(debug=True)
