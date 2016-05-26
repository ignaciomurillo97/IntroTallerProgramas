#programa que dice el mayor de dos numeros

a = input("numero a: ")
b = input("numero b: ")

while not(a.isnumeric() and b.isnumeric()):
  print("sea serio y ponga numeros:")
  a = input("numero a: ")
  b = input("numero b: ")

a = float(a)
b = float(b)

if (a < b):
  print(b)
else:
  print(a)

