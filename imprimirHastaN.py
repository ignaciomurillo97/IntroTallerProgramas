#inprimir pares hasta n
def Pares(m, n):
  if (isinstance(n, int) and m < n):
    
    while (m <= n):
      if(m%2 == 0):
        print(m)
      m += 1
  else:
    print("no es un numero entero")

  return



Pares(-4, 40)
