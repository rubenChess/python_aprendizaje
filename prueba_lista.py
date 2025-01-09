lista = [1,2,3,4,5,6,7]
def sumar_lista():
	contador = 0 # Alineado correctamente dentro de la función
	aux = 0
	for numeros_de_lista in lista:
		contador += numeros_de_lista # Alineado dentro del bucle for
		aux += 1
		print(contador) # Alineado dentro del bucle for
	print(f"la suma de lista de numeros es: {contador} \n ")
	promedio_numeros(contador,aux)
	
def promedio_numeros(suma_total , cantidad_numeros):
	print(f"El promedio de la lista de numeros es: {suma_total/cantidad_numeros} \n ")

def lista_pares_encontrados():
	pass
	print(f"La lista de pares encontrados es: ??? \n ")

def mostrar_resultados_anteriores():
	pass
	print(f"Aquí tienes todos los resultados anteriores: ??? \n ")
	sumar_lista()
	promedio_numeros()
	lista_pares_encontrados()
    

# Ahora llamamos a la función
sumar_lista()
lista_pares_encontrados()
mostrar_resultados_anteriores()