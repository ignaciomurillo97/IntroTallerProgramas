a = input("pongame algo!: ")

while (a != "Salir"):
  if a.isnumeric():

    if int(a)< 20:
        print("es menor")

    else:
        print("es mayor")

  else:
      print("debe ingresar un valor numerico")
  a = input("pongame algo!: ")

print("Hasta Luego")
        
