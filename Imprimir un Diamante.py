#Imprimir un Diamante

def ImprimirFila(anchoActual, anchoTotal):
	if (isinstance(anchoTotal, int)):
		diferencia = anchoTotal - anchoActual
		textoFila=""
		for i in range(0, diferencia):
			textoFila += " "

		textoFila += "*"

		for i in range(0, anchoActual - 2):


n = input("diametro del Diamante: ")
#revisar si n es impar
if (isinstance(n, int), n%2==1):
	print("n es impar")

i = 1
n = int(n)
#incrementar el ancho del diametro cada nivel
while (i < n):
	print(i)
	i += 2
#reducir el ancho del diametro hasta llegar a 1
while (i > 0):
	print(i)
	i -= 2 
