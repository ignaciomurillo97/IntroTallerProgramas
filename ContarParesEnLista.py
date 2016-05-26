#reciba una lista de enteros y retorna la cantidad de enteros

def contarParesEnLista(inLista):
    if (not isinstance(inLista, list)):
        print("invalido")
    else:
        contador = 0
        for i in inLista:
            if i % 2 == 0:
                contador += 1

        return(contador)
