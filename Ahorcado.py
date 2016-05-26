# -*- coding: utf-8 -*-

caracteres_especiales =''

estadoAhorcado = ["---  \n|    \n|    \n|    \n", "---  \n|  0 \n|    \n|    \n", "---  \n|  0 \n|  | \n|    \n", "---  \n|  0 \n| /| \n|    \n", "---  \n|  0 \n| /|\\\n|    \n", "---  \n|  0 \n| /|\\\n| /  \n", "---  \n|  0 \n| /|\\\n| /\\ \n"]

## Funcuion que Corre un juego de Ahorcado.
## Entradas:
##  -La Palabra que el jugador tratara de adivinar (se pasa por consola, no por argumeto)
## Salida:
##  -Juego de Ahorcado

def Ahorcado ():
    continuar = True
    while continuar == True:

        palabra_original = input('Cual palabra desea usar: ')
        caracteres_especiales = encontrar_caracteres_especiales(palabra_original)
        palabra = formatear_palabra(palabra_original)
        intentos = 0
        letrasIntentadas = ' '
        juegoGanado = False

        print('\n' * 50)

        while intentos < 7 and not juegoGanado:
            ## imprimir estado del juego
            print("\n" * 30)

            print(estadoAhorcado[intentos])

            print("Letras usadas: " + letrasIntentadas + " ")

            print("\n")

            imprimir_campos(palabra_original, palabra, letrasIntentadas, caracteres_especiales)
            letra = input('que letra quiere intentar? ').lower()


            ## evaluar entrada del ususario
            if len(letra) > 1:
                print("solo puede introducir una letra a la vez.")

            elif letra in letrasIntentadas:
                print('Ya uso esa letra...')

            elif letra not in palabra:
                print('Letra incorrecta!')
                intentos += 1
                letrasIntentadas += letra

            else:
                print('letra corecta!')
                letrasIntentadas += letra

            ## el juego ha sido ganado?
            juegoGanado = True
            for i in palabra:
                if i not in letrasIntentadas and i not in caracteres_especiales:
                    juegoGanado = False


        ## revisar si gano
        if not juegoGanado:
            print('Ha perdido...')
        else:
            print('Felicidade. Ha ganado!')
            print('la palabra o frase era: ' + palabra_original)

        ## volver a jugar
        if input('Desea volver a jugar? (y/n)') == 'n':
            continuar = False

## Retorna todos los carateres especiales de la palabra (caracter especal como cualquier caracter que su .isalpha() sea Falso)
## Entrada:
##  -String en la cual se buscaran los caracteres especiales
## Salida:
##  - String con los caracteres especiales presentes en la palabra.
def encontrar_caracteres_especiales (palabra):
    caracteres_especiales = ''
    for i in palabra:
        if not i.isalpha():
            caracteres_especiales += i

    return caracteres_especiales

## Imprime las letras adiviadas y espacios donde esta las que n se han adivinado
## Entrada:
##  - Palabra Origial
##  - Palabra (la palabra original pero sin tildes ni mayusculas)
##  - Letras Intentadas (todas las letras que el jugador ha ingresado)
##  - Caracteres especiales presentes en la palabra.
## Salida:
##  - imprime "_ " donde hay una letra que aun no haya sido adivinada y la
##    Letra donde si haya sido adivinada

def imprimir_campos (palabra_original, palabra, letras_intendatas, caracteres_especiales):
    msg = ''
    for i in range(len(palabra)):
        if palabra[i] in letras_intendatas or palabra[i] in caracteres_especiales:
            msg += palabra_original[i] + ' '
        else:
            msg += '- '

    print(msg)

## Cambia las mayusculas y las tildes de una palabra.
## Entrada:
##  - La palabra a la cual se le quieran quitar las tildes y mayuscula.
## Salida:
##  - La palabra sin tildes ni mayusculas.
    
def formatear_palabra(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace('á', 'a')
    palabra = palabra.replace('é', 'e')
    palabra = palabra.replace('í', 'i')
    palabra = palabra.replace('ó', 'o')
    palabra = palabra.replace('ú', 'u')
    return palabra

Ahorcado()
