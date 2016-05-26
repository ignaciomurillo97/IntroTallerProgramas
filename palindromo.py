from InvertirNumeroEntero import invertir

#devuelve true si el numero es palindromo:
#entrada: N un umero entero
#salida: true o false

def revisarPalindromo (n):
    if (isinstance(n, int) and n > 0): 
        return n == invertir(n)
    else:
        return "Debe ser un numero positivo"


