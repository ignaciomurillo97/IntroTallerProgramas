a = input("Variable A: ")
b = input("Variable B: ")

while (not a.isnumeric() and not b.isnumeric()):
  print("No son numeros!")
  a = input("Variable A: ")
  b = input("Variable B: ")
  
a = int(a) + int(b)
b = int(a) - int(b)
a = int(a) - int(b)

print("El valor de A: ", a)
print("El valor de B: ", b)
