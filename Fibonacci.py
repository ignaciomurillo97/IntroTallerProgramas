#calcular el elemento de fibonacci en la posicio n
#entrada: numero entero que servira de limite 
#

def fibonacci (n):
    if not isinstance(n, int):
        return "Debe ser un numero entero positivo"
    
    fibTrasAnterior = 0
    fibAnterior = 1
    fibActual = 1

    if n == 0:
        return 0
        
    for i in range(2, n):
        fibTrasAnterior = fibAnterior
        fibAnterior = fibActual
        fibActual = fibTrasAnterior + fibAnterior
        '''
    i = 2  
    while i < n:
        fibTrasAnterior = fibAnterior
        fibAnterior = fibActual
        fibActual = fibTrasAnterior + fibAnterior
        #print(fibActual)
        i += 1
        '''
    return fibActual
