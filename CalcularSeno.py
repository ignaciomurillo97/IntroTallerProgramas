def fectorial(n):
    resultado = 1
    for i in range(1, (n + 1)):
        resultado *= i
    return resultado

def calcularSeno(x, n):
    resultado = 0 
    for i in range(0, n):
        resultado += (-1)**i * (x)**(2 * i + 1) / fectorial(2 * i + 1)

    return resultado

        
