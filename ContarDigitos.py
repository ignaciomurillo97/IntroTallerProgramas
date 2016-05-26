#Contar Digitos

def ContarDigitos(n):
  if (isinstance(n, int)):
    digitos = 0

    while (n > 0):
      n //= 10
      digitos += 1
    return digitos
  
  else:
    print("no es un numero entero")

print("resultad", ContarDigitos(123456789))
