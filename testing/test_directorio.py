import pytest
from flask import Flask
from app import app

# hara que nuestra variable sea accesible en todo el archivo
@pytest.fixture()
def cliente():
    # metodo que flask brinda para poder hacer un testing sin levantar un servidor como tal
    yield app.test_cliente()

def test_publicaciones_get (cliente):
    resultado = cliente.get("/publcaciones")
    assert resultado.status_code == 200
    assert resultado.json == {
        "content":[]
    }