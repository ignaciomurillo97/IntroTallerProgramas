#programa que calcula el mayor de 3 numeros

a = input("a: ")
b = input("b: ")
c = input("c: ")

while (not a.isnumeric() and not b.isnumeric() and not c.isnumeric()):
  print("Esos no son numeros...")
  a = input("a: ")
  b = input("b: ")
  c = input("c: ")

a = float(a)
b = float(b)
c = float(c)

if (a > b):
  if (a > c):
    print(a)
  else:
    print(c)
elif (b > c):
  print(b)
else:
  print(c)
  
