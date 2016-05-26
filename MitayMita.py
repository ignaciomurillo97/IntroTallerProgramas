#recibir ds strings e imprimir mitad y mitad concatenado

def mesclarString(inStringA, inStringB):
    if (not isinstance(inStringA,str) and not isinstance(inStringB, str)):
        print("etrada no es un string")
    else:
        mitadA = len(inStringA) // 2
        mitadB = len(inStringB) // 2
        print(inStringA[:mitadA] + inStringB[mitadB:])
        print(inStringB[:mitadB] + inStringA[mitadA:])
