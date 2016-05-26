#colocoar en medio de un string en otro string

def insertarSting(stringA, stringB):
    if(not isinstance(stringA, str) or not isinstance(stringB, str)):
        print("las entradas deben ser string")
    else:
        mitadStringA = len(stringA) // 2
        print(stringA[:mitadStringA] + stringB + stringA[mitadStringA:])
