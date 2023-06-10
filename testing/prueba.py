import requests
def sumar(a,b):
    return a + b

def saludar():
    saludo = saludoCordial()
    return saludo


def saludoCordial():
    return " muy buenas noches ante ustedes"

def get_pokemones(nombre):
    resultado =requests.get('https://pokeapi.co/api/v2/pokemon/pikachu/{nombre}')
    if resultado.status_code == 200:
        return resultado.json()
    else :
        return "Error con la API" 