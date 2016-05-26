def sumaVectores (v, w):
    if not isinstance(v, list):
        return 'la v debe ser un vector'
    if not isinstance(w, list):
        return 'la w debe ser un vector'
    if not all (isinstance(x, (float, int)) for x in v):
        return "todos los elementos de v deben ser ints o floats"
    if not all (isinstance(x, (float, int)) for x in w):
        return "todos los elementos de w deben ser ints o floats"
    if len(v) != len(w):
        return 'las listas deben ser de igual tamaño'

    pruebaRes = [v[i] + w[i] for i in range(len(w))]

    return pruebaRes


def productoEscalar (v, e):
    if not isinstance(v, list):
        return 'la v debe ser un vector'
    if not isinstance (e, (float, int)):
        return  'el escalar debe ser un numero'
    if not all (isinstance(x, (int, float)) for x in v):
        return 'los valores del vector deben ser ints o floats'

    return [v[i] * e for i in range(len(v))]


def multiplicarVector(v, w):
    if not isinstance(v, list):
        return 'la v debe ser un vector'
    if not isinstance(w, list):
        return 'la w debe ser un vector'
    if not all (isinstance(x, (float, int)) for x in v):
        return "todos los elementos de v deben ser ints o floats"
    if not all (isinstance(x, (float, int)) for x in w):
        return "todos los elementos de w deben ser ints o floats"
    if len(v) != len(w):
        return 'las listas deben ser de igual tamaño'


    return sum([v[i] * w[i] for i in range(len(w))])



