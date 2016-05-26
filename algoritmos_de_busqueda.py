import AlgoritmosOrdenamiento

## busqueda secuencial

## busqueda bimaria

def busqueda_binara (lista, buscado):
    def busqueda_binaria_aux (lista, buscado, menor, mayor):
        if menor > mayor:
            return -1

        mitad = (mayor + menor) // 2

        if lista[mitad] == buscado:
            return mitad

        if buscado < lista[mitad]:
            return busqueda_binaria_aux(lista, buscado, menor, mitad - 1)

        return busqueda_binaria_aux(lista, buscado, mitad + 1, mayor)

    if isinstance(lista, list):
        return busqueda_binaria_aux(lista, buscado, 0, len(lista) - 1)
    else:
        return "debe ser una lista ordenada"

## busqueda por interpolacion

def busquedaInterpolacion (lista, buscado):
    def busquedaInterpolacionAux (lista, buscado, menor, mayor):
        if menor > mayor:
            return -1
        else:
            mitad = int(menor + (buscado - lista[menor]) * ((mayor - menor)/(lista[mayor])))
            if lista[mitad] == buscado:
                return mitad
            if buscado < lista[mitad]:
                return busquedaInterpolacionAux(lista, buscado, menor, mayor - 1)
            return busquedaInterpolacionAux(lista,buscado, mitad + 1, mayor)


    if isinstance(lista, list):
        return 'entrada invalida'

    else:
        return busquedaInterpolacionAux(lista, buscado, 0, len(lista) - 1)

busquedaInterpolacion([1,2,3,4,5,6,7,8,9,10], 10)



