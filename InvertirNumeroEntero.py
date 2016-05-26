#invertir enteros

def invertir(n):
  if(isinstance(n, int) and n > 0):
    inverso = 0
    while (n > 0):
      inverso = inverso * 10 + n % 10
      n //= 10
 
    return(inverso)

  else:
    print("ENTEROS Y MAYORES A CERO!!!!!!")


    
