def esPalindromo(inString):
    if (not isinstance(inString, str)):
        print("entrada no es string")
    else:
        inString = inString.lower()
        inString = inString.replace(" ", "")
        if (inString == inString[-1:-len(inString) - 1:-1]):
            print("es palindromo")
        else:
            print("no es palinromo")

            
