import turtle
import math
import Fibonacci

def hacerPoligono (lados, dist):
    angulo = 360/lados

    i = 0
    while i < lados:
        turtle.fd(dist)
        turtle.rt(angulo)
        i += 1

def forma(cantidad, poligono, distancia):
    angulo = 360/cantidad

    j = 0
    while j < cantidad:
        hacerPoligono(poligono, distancia)
        turtle.rt(angulo)
        j += 1


def cuartoDePoligono (lados, dist):
    angulo = 360/lados

    i = 0
    while i < lados /4:
        turtle.fd(dist)
        turtle.rt(angulo)
        i += 1


def segmento (radio, cantidad):
    angulo = 10
    lado = radio * math.sin(math.degrees(angulo))

    i = 0 
    while i < 360 / cantidad:
        turtle.fd(lado)
        turtle.rt(angulo)
        i += angulo

def crearFibonacci (cantidad):
    i = 0
    while i < cantidad:
        radio = Fibonacci.fibonacci(i)
        segmento (radio, 4)
        i += 1

        
    
    

