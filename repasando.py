lista_numeros = [1,2,3,4,5,6,7,8,9,10]
def sumar_lista_numeros():
	contador_iteraciones=0
	for tomar_cada_numero_lista in lista_numeros:
		print (f"Voy en la Iteración #{contador_iteraciones}")
		print (f"Estaremos tomando cada numero de la lista: {tomar_cada_numero_lista}")
        contador_iteraciones = contador_iteraciones + 1
sumar_lista_numeros()