numero = input("Numero: ")

while(not numero.isnumeric()):
  print("Eso no es un numero!")
  numero = input("Numero: ")

numero = int(numero)

while (numero >= 999 or numero <= 100):
  print("Numero no valido!")
  numero = input("Numero: ")

digitoMasSignificativo = numero // 100
print(digitoMasSignificativo)

digitoMenosSignificativo = numero % 10
print(digitoMenosSignificativo)

digitoDelMedio = (numero % 100)//10
print(digitoDelMedio)

nuevoNumero = digitoMenosSignificativo * 100 + digitoDelMedio * 10 + digitoMasSignificativo
print(nuevoNumero)

if (digitoMasSignificativo == digitoMenosSignificativo):
  print("el primer y ultimo digito son iguales")

