import math

def fib(n):
	a, b = 0, 1
	resultado = [a]
	for i in range(n):
		resultado.append(b)
		a, b = b, a + b
	return resultado

#print(fib(25))


def cribaEratostenes (m):
	numeros = list(range(1,m))
	numerosPrueba = list(range(2,int(math.sqrt(m)) + 1))
	noPrimos = []
	
	for i in numerosPrueba:
		noPrimos = [x for x in numeros if x % i == 0]

		for i in noPrimos:	
			if i in numeros and i != noPrimos[0]:
				numeros.remove(i)

	print numeros



cribaEratostenes(100)