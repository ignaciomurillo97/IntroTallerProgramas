# funcion que recibe una lista de enteros y retorna true si los numeros vienen ordenados
# de forma acendente y false si no

def esAcendente(inLista):
    if (not isinstance(inLista, list)):
        print("invalido")
    for i in inLista:
        if (not isinstance(i,float) and not isinstance(i,int)):
            return("todos deben ser numreos")

    else:
        valorAnterior = inLista[0]
        for i in inLista:
            if valorAnterior > i:
                return(False)

            else:
                valorAnterior = i

        return(True)

