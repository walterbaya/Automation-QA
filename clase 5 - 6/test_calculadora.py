import pytest  #importamos el modulo de pytest
##import calculadora.py #importamos el nombre del archivo que queremos tester
##si usamos el import de arriba trae todo hasta la funcon main.
##vamos a importar las funciones que utilizaremos nada mas.
from calculadora import suma, resta, multiplicacion, division 


#es obligatorio que la clase de test empiece como _test y lo mismo para las funciones
def test_suma():
    #assert valida los resultados esperados con los obtenidos.
    assert suma(2, 3) == 5
    assert suma(5, 8) == 1

#para correr la prueba py -m pytest -v test_calculadora.py
#podria ser sin la -v para que sea menos detallado.

#Parametrizacion de funciones
@pytest.mark.criticos
@pytest.mark.parametrize("a,b,resultado", [
    (10,5,15),
    (1,-1,0),
    (2,4,6)
])
def test_suma(a,b,resultado):
    assert suma(a,b) == resultado

#trabajar con errores

#crear etiquetas personalizadas para casos de prueba
#necesitamos el pytest.ini
@pytest.mark.manejoError
def test_division_cero():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)

#py -m pytest -v -m criticos me va a ejecutar solo los que tengan la mark criticos

#podemos saltearnos tests tambien
#skipeamos la prueba utilizando lo siguiente
@pytest.mark.skip(reason = "funcionalidad no implementada")
def test_resta():
    assert resta(2,3) == 5

#el numero debe aproximarse a otro 1e-1 es el porcentaje de tolerancia en notacion cientifica
def test_division_decimal():
    assert division(10,3) == pytest.approx(3.33333, rel=1e-3)


#py -m pip install pytest-html
#es el modulo para generar archivos html
#utilizamos un comando para generar los tests
#py -m pytest --html=report.html 
#va a generar un archivo de nombre report.html