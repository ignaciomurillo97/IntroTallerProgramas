import math
#econtrar el x de una ecuacion cuadratica ax**2 + bx + c
#entrada: a, b, c donde todos son reales
#salida x
#a debe ser diferente de 0

def calcularDiscriminante(a, b, c):
    discriminante = b**2 - 4*a*c
    return discriminante

def calcularEcuacion(a, b, c):
    if (isinstance(a, int) and isinstance(b, int) and isinstance(b, int)):
        if (a != 0):
        
            discriminante = calcularDiscriminante(a, b, c)

            if (discriminante < 0):
                return ("no hay solucion real")
            elif (discriminante == 0):
                print( -b + math.sqrt(discriminante) / 2 * a)
            else:   
                x1 = (-b + math.sqrt(discriminante)) / (2 * a)
                x2 = (-b - math.sqrt(discriminante)) / (2 * a)
                print(x1, x2)

        else:
            print("a debe de ser diferente de 0")
