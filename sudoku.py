
m=[[1,2,3,4,5,6,7,8,9],[2,3,4,5,6,7,8,9,1],[3,4,5,6,7,8,9,1,2],[4,5,6,7,8,9,1,2,3],[5,6,7,8,9,1,2,3,4,],[6,7,8,9,1,2,3,4,5],[7,8,9,1,2,3,4,5,6],[8,9,1,2,3,4,5,6,7],[9,1,2,3,4,5,6,7,8]]
m1=[[5, 3, 4, 6, 7, 8, 9, 1, 2],[6, 7, 2, 1, 9, 5, 3, 4, 8],[1, 9, 8, 3, 4, 2, 5, 6, 7],[8, 5, 9, 7, 6, 1, 4, 2, 3], [4, 2, 6, 8, 5, 3, 7, 9, 1], [7, 1, 3, 9, 2, 4, 8, 5, 6], [9, 6, 1, 5, 3, 7, 2, 8, 4],[2, 8, 7, 4, 1, 9, 6, 3, 5],[3, 4, 5, 2, 8, 6, 1, 7, 9]]
m2=
def columna(matriz, col):
    return [matriz[i][col] for i in range(len(matriz))]

def sudokuRevizarFila(fila):
    if any(fila.count(x) > 1 or x>9 or x<1 for x in fila):
        return False
    return True

def obtenerRegion(matriz, region):
    x = region%3 * 3
    y = region//3 * 3
    nuevaregion = []
    for i in matriz[y:y+3]:
        nuevaregion += i[x:x+3]
    return nuevaregion



def sudoku (matriz):
    ## revizar fila
    for i in matriz:
        if not sudokuRevizarFila(i):
            return "fila: " + str(i)

    ## revizar columna
    for i in range(len(matriz[0])):
        columnaActual = columna(matriz, i)
        if not sudokuRevizarFila(columnaActual):
            return "columna: " + i

    ## revizar region
    for i in range(9):
        if not sudokuRevizarFila(obtenerRegion(matriz, i)):
            return sudokuRevizarFila(obtenerRegion(matriz, i))
    return True

print(sudoku(m1))