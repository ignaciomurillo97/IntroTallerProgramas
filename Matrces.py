from Vectores import *

def esMatriz (matriz):
    if not isinstance(matriz, list):
        return False
    for i in range(len(matriz)):
        if not isinstance(matriz[i], list):
            return False
        if not all(isinstance(x, (float, int)) for x in matriz[i]):
            return False

        if len(matriz[i]) != len(matriz[i-1]):
            return False

    return True

def sumaMatrices (M1, M2):
    if not esMatriz(M1) or not esMatriz(M2):
        return

    if len(M1) != len(M2):
        return

    if len(M1[0]) != len(M2[0]):
        return

    resultado = []
    for i in range(len(M1)):
        resultado.append(sumaVectores(M1[i], M2[i]))

    return resultado

def columna (matriz, col):
    if not esMatriz(matriz):
        return 'se esoeraba una matriz'
    if len(matriz[0]) <= col:
        return 'no vale pedir una columna que no existe'

    return [matriz[x][col] for x in range(len(matriz))]

def transpuesta (matriz):
    if not esMatriz(matriz):
        return 'se esoeraba una matriz'

    return [columna(matriz, x) for x in range(len(matriz[0]))]

def multiplicarVectorMatriz(v, m):
    if not esMatriz(m) and len(v) == len(m):
        return
    resultado = []
    for c in range(len(m[0])):
        resultado += [multiplicarVector(v, columna(m, c))]

    return resultado

##las columnas de 'a' debe ser igual a las filas de 'e'

def multiplicacionMatrices (m1, m2):
    if not esMatriz(m1) or not esMatriz(m2) or not len(m1[0]) == len(m2):
        return

    resultado = []
    for f in range(len(m1)):
        filaRes = []
        for c in range(len(m2[0])):
            filaRes += [multiplicarVector(m1[f], columna(B, C))]
        resultado += [filaRes]
        return resultado

### Ejercicios de vectores de matrices

def reflejoHorizontal (matriz):
    resultado = []
    for i in matriz:
        resultado += [i[::-1]]

    return resultado

def reflejoVerticall(matriz):
    return matriz[::-1]

def maximosFila (matriz):
    resultado = []
    for fila in matriz:
        mayorFila = fila[0]
        for elemento in fila:
            if elemento > mayorFila:
                mayorFila = elemento
        resultado.append(mayorFila)

    return resultado

def diagonalMatrizCuadrada (matriz):
    if len(matriz[0]) != len(matriz):
        return 'la matriz no es cuadrada'

    resultado = []
    for i in range(len(matriz)):
        resultado.append(matriz[i][i])
    return resultado

def ceros (matriz):
    resultado = []
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == 0:
                resultado.append([fila, columna])

    return resultado

def clasificacionDeMatriz(matriz):
    ## cuadrada
    resultado = []
    if len(matriz) == len(matriz[0]):
        resultado += ['cuadrado']
    if all ( all(x == 0 for x in i) == True for i in matriz):
        resultado += ['nula']

    identidad = True
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] != 1 and fila == columna:
                identidad = False
            if matriz[fila][columna] != 0 and fila != columna:
                identidad = False

    if identidad:
        resultado += ['identidad']

    return resultado


M1 = [[1,2,3], [4,5,6], [7,8,9]]
M2 = [[0, 2, 3], [4, 0, 6], [7, 8, 0]]
M3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(clasificacionDeMatriz(M3))
