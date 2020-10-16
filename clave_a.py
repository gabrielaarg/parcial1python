import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 2 numeros
2+4 = 6
"""


# start-->
def suma():
    suma= 2+4
    return suma


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros pares del 1 al 1000
"""


# start-->
def sumaPares():
    result = 0
    contador = 0
    while contador <=1000:
        if (contador%2==0):
            result = result + contador
        contador = contador + 1    
    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el area total de superficie de un cilindro
radio = 5 m
altura = 7 m
area lateral: 2*pi*r*a
area circulo: 2*pi*r^2
area total: area lateral + area circulo
"""


# start-->
def areaTotalCilindro():
    totalarea= round((areaLateral() + areaCirculo()),2)
    return totalarea


def areaLateral():
    rad= 5.0
    h= 7.0
    result = (2.0*math.pi*rad*h)
    return result


def areaCirculo():
    rad = 5.0
    result = (2.0*math.pi*rad**2)
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Cilindro:
    def areaTotalCilindro(self):
        totalarea= round((areaLateral() + areaCirculo()),2)
        return totalarea


    def areaLateral():
        rad= 5.0
        h= 7.0
        result = (2.0*math.pi*rad*h)
        return result


    def areaCirculo():
        rad = 5.0
        result = (2.0*math.pi*rad**2)
        return result

        

"""
***************************************************************
@@ ejercicio 5 @@
restaurante de pizzas
pizza
    nombre
    lugar
    costo
    conDescuento
    descuento
"""


class Restaurante:



    def ordenar(self):
         pass


    def costoTotal(self):
        return 0

    def costoTotalConDescuento(self):
        return 0


class Pizza:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return "https://github.com/gabrielaarg/parcial1python.git"
