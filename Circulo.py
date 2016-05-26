import  math

def traducirParOrdenadoALineal(inX, inY, columnas):
    lineal = (inY - 1) * columnas + inX
    return (lineal)

def insertarString(inString, caracter, posicion):
    if (isinstance(posicion, int)):
        newString = inString[:(posicion - 1)] + caracter + inString[posicion:]
        return newString

def imprimirMatriz(inMatriz, columnas):
    i = 0
    while i < columnas:
        #inicioImpresion = traducirParOrdenadoALineal(0, i, columnas)
        fila = inMatriz[i * columnas:(i+1)*columnas]
        print(fila)
        i += 1

def CrearCirculo(resolucion, correccion):
    anguloActual = 0
    i = 0

    matriz = " " * (((resolucion + correccion) * 4)**2)

    anguloPorSegmento = 360 / (resolucion  * 2 * math.pi)

    while anguloActual < 360:
        radioActual = resolucion + abs(math.cos(math.radians(anguloActual))) * correccion
        #print(radioActual)
        x = int(math.cos(math.radians(anguloPorSegmento * i)) * radioActual) * 2
        y = int(math.sin(math.radians(anguloPorSegmento * i)) * radioActual)
        #print(x, ", ", y)
        anguloActual += anguloPorSegmento
        matriz = insertarString(matriz, "*", traducirParOrdenadoALineal(x + (resolucion + correccion) * 2, y + (resolucion + correccion), (resolucion + correccion) * 4))
        i += 1
    imprimirMatriz(matriz, (resolucion + correccion) * 4)


radio = 0

radio = input("Radio del Circulo: ")

while not radio.isnumeric():
    print("radio debe ser un numero")
    radio = input("Radio del Circulo: ")

radio = int(radio)

while radio <= 0:
    print("Radio no puede ser menor o igual a 0")
    radio = input("Radio del Circulo: ")

CrearCirculo(radio, 0)

