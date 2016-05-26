#sumar de 1 a n
n = input("cantidad de sumas a realizar: ")

def Sumatoria(numero):
  if isinstance(numero, int) and numero > 0:
    
    resultado = 0;
    for i in range(1, (numero + 1)):
      resultado += i
    return resultado
  print("debe ser numero positivo")


while (not n.isnumeric()):
  print("Solo Numeros")
  n = input("cantidad de sumas a realizar: ")

n = int(n)

res = Sumatoria(n)

print(res)
  
