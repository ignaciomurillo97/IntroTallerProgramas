

def sumatoria (n):
    def sumatoriaAux(resultado, n):
        if n == 1:
            return resultado
        else:
            return sumatoriaAux (n + resultado, n -1)

    if isinstance(n, int) and n > 0:
        return sumatoriaAux(1, n)
    else:
        return "debe ser mayor a cero"



def sumarDigitos(n):
    if not isinstance(n, int):
        return "etrada debe ser entera"

    def sumarDigitosAux(n, resultado):
        if n == 0:
            return resultado
        else:
            return sumarDigitosAux(n // 10, resultado + n % 10)

    return sumarDigitosAux(n, 0)


def invertirNumero (n):
    if not isinstance(n, int):
        return "etrada debe ser entera"

    def invertirDigitosAux(n, resultado):
        if n == 0 :
            return resultado
        else:
            return invertirDigitosAux(n // 10, resultado * 10 + n % 10)

    return invertirDigitosAux(n, 0)

def mayorDeUnaLista (lista):
    if not isinstance(lista, list):
        return "la entrada debe ser una lista"
    for i in lista:
        if not (isinstance(i, int) and isinstance(i, float)):
            return "los elementos de la lista deben ser ints"
    def aux (lista, mayor):
        if len(lista) == 0:
            return mayor
        else:
            if lista[0] > mayor:
                mayor = lista[0]
            return aux(lista[1:], mayor)
    return aux(lista, 0)


def insertarEnListaOrdenada (lista, elemento):
    if not isinstance(lista, list):
        return "la entrada debe ser una lista"
    for i in lista:
        if not isinstance(i, int) and isinstance(i, float):
            return "los elementos de la lista deben ser ints"
    if not isinstance(elementos, int)
        return "el eleme a insertar debe ser un int"    

    