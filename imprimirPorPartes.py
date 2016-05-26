def imprimirPorPartes(inString):
    if (not isinstance(inString, str)):
        print("entrada no string")
    else:
        print(inString[0: :2])
        print(inString[1: :2])
