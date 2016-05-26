#programa que le pide un string al usuario y develve n cantidad de caracteres

def imprimirCaracteres(inString, n):
    if (not isinstance(inString, str) and not isinstance(n, int)):
        print("entrada no valida")
    elif (n < 0 or n > len(inString)):
        print("n esta fuera del rango aceptable")
    else:    
        print(inString[:n])

    
        

