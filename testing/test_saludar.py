import testing.prueba


def mock_saludoCordial():
    return "Hola!!!"


def test_saludar(monkeypatch):
    #monkeypatch > me dara la infomacion de donde esoty haciendo testing
    print(monkeypatch)
    # setattr > primer parametro le diremos que queremos modificar (archivo o un modulo), segundo parametro indicaremos que funcion o metodo queremos modificar, tercer parametro el nuevo comportamiento de el segundo parametro indicado
    monkeypatch.setattr(testing.prueba, "saludoCordial", mock_saludoCordial)
    resultado = testing.prueba.saludar()

    assert resultado == "Hola!!!"


def test_saludo_con_cordialidad():
    resultado = testing.prueba.saludar()

    assert resultado == " muy buenas noches ante ustedes"
