import validaciones

def test_intentos_nombres1():
    assert validaciones.vnombre("Franco Ferreyra")
    
def test_intentos_nombres2():
    assert validaciones.vnombre("243")

def test_intentos_telefono():
    assert validaciones.vtelefono("5493434695566")

    