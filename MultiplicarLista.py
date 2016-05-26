#multiplicar todos los elementos de una lista
def multiplicarLista(inLista):
    if (not isinstance(inLista, list)):
        return "invalido"
    else:
        resultado = 1
        for i in inLista:
            resultado *= i

    return resultado

