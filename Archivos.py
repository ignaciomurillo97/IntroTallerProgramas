import json

## abrir un archivo

#archivo = open("Hola.txt", "r") ## la variable archivo ahora es el device handler en modo lectura
## modo lectura solo se puede leer

## si no existe el archivo, da error

#archivo = open("Hola.txt", "w") ## crea el archivo en modo escritura y si ya existe lo borra y lo vuelve a
## crear

#archivo = open("Hola.txt", "w") ## lo abre en modo escritura perono lo borra y pone la posicion actual al final
## del archivo (agregar datos)

#archivo.close()
## los cambios en el archivo a veces solo se guardan en el cierre del archivo

## s = archivo.read(n) ## lee n bytes del archivo
## s = archivo.read() ## lee el archivo completo

## s = archivo.readline() ## lee datos hasta encontrar un enter "\n"

## los file handlers son interables. podemos recorrer sus lineas,ej:

## for linea in archivo:
##   print (linea)

## crear una lista de las lineas del archivo:

## list = list(archivo)

## list = arcivo.readlines()

## EOF = end of file
## BOF = begining of file



## las siguientes funciones se usan principalmente en modo binario, en modo texto puede dar comportamiento
## inesperado


## Write escribe contenidos en el arcivo usando la posicion actual
## si la posicion esta al final del archivo le agrega datos al archivo,
## en modo texto recibe un string
## en modo binario recibe un objeto 'bytes'
## e pyton se deben convertir las varables u objetos a string o bytes para poder escribirlos


## arcivo.seek(offset, fromwhat)
## offset, cantidad bytes que deseo moverme (puede ser negativo)
## fromwhat, desde donde:
##    0 -> desde el inicio
##    1 -> desde la posicion actual
##    2 -> desde el final

## archivo.tell() ## posicion actual desde el inicio del archivo

## JSON:
## se usa para convertir a y desde JS object notation:

## Funciones :

## json.dump(objeto, archivo) ## escribe el objeto

## x = json.load(archivo) ## lee un objeto