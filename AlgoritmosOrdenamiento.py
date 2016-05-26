import random
import datetime

## bubble sort
def bubble_sort_basico (lista):
    if not (isinstance(lista, list)):
        return "entrada debe ser una lista"

    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j],lista[j + 1] = lista[j + 1], lista[j]

    return lista


## insertion sort
def insert_sort (lista):
    lista_ordenada = []

    for i in lista:
        lista_ordenada = insertar_en_lista(lista_ordenada, i)

    return lista_ordenada

def insertar_en_lista (lista, elemento):
    i = 0
    insertado = False

    if lista == []:
        return [elemento]

    if elemento < lista[0]:
        return [elemento] + lista

    while i < len(lista) and not insertado:
        if elemento < lista[i]:
            lista = lista[:i] + [elemento] + lista[i:]
            insertado = True
        i += 1

    if not insertado:
        lista.append(elemento)

    return lista

## selection sort
def menor (lista):
    if (not isinstance(lista, list)):
        return 'debe ser una lista'

    variable_menor = 0
    for i in range(len(lista)):
        if lista[i] < lista[variable_menor]:
            variable_menor = i

    return variable_menor

def selection_sort(lista):
    if not isinstance(lista, list):
        return 'entrada invalida'
    if lista == []:
        return 'la lista no puede ser vacia'

    lista_resultado = []
    while len(lista) > 0:
        elemento_menor = menor(lista)
        lista_resultado += [lista[elemento_menor]]
        lista[elemento_menor] = lista[0]
        lista = lista[1:]

    return lista_resultado

## merge sort
def merge (lista1, lista2 ):
    resultado = []
    while len(lista1) != 0 and len(lista2) != 0:
        if lista1[0] < lista2[0]:
            resultado.append(lista1[0])
            lista1 = lista1[1:]
        else:
            resultado.append(lista2[0])
            lista2 = lista2[1:]

    resultado += lista1 + lista2
    return resultado

def mergeSort (lista):
    if len(lista) <= 1:
        return lista
    else:
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]
        izquierda = mergeSort(izquierda)
        derecha = mergeSort(derecha)
        resultado = merge(izquierda, derecha)
        return resultado

## quick sort (Anthony Hoare 1965)
def quick_sort (lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        lista = lista[1:]

        menores = [x for x in lista if x < pivote]
        mayores = [x for x in lista if x >= pivote]
        menores = quick_sort(menores)
        mayores = quick_sort(mayores)
        return menores + [pivote] + mayores

##Bogo Sort
def bogo_sort(lista):
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                ordenado = False

        if not ordenado:
            random.shuffle(lista)

    return lista

def generar_lista_rand(n):
    lista = []

    for i in range(n):
        lista.append(random.randrange(n))

    return lista

def medir_duracion (funcion, lista):
    tiempoInicial = datetime.datetime.now()
    funcion(lista)
    tiempoFinal = datetime.datetime.now()
    print("duracion: ", tiempoFinal - tiempoInicial)



medir_duracion(bogo_sort, generar_lista_rand(16))
