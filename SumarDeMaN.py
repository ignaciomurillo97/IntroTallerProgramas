#sumar d m a n
#m = input("m: ")
#n = input("n: ")
#
#while(not m.isnumeric() and not n.isnumeric()):
#  print("NUMEROS ETEROS!")
#  m = input(m)
#  n = input(n)
#  
#m = int(m)
#n= int(n)

def sumatoria(M, N):
    if isinstance(M, int) and isinstance(N, int):
        if M >= 0 and N > 0 and M < N:
            resultado = 0
            i = M

            while (i <= N):
                resultado += i
                i += 1

            return  resultado
        else:
            return "M y N deben ser enteros positivos. y M < N"

    else:
        return "los valores de M y N deben ser numeros eneteros"


#print (sumatoria(m, n))
