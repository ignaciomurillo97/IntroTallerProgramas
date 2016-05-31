def fibonachiMemo(n):
    resultados = {}

    def fibonachiMemoAux(n):
        if  <= 1:
            return 1
        if n in resultados:
            return resultados[n]

        res = fibonachiMemoAux(n-1) + fibonachiMemoAux(n-1)
        resultados[n] = res
        return res

    if isinstance(n, int):
        return fibonachiMemoAux(n)
    else:
        return "debe ser un numero positivo"
