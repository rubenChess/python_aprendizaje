lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sumar_lista_numeros():
    contador_iteraciones = 0
    suma_de_cada_numero_lista=0
    print(f"la lista de numeros es esta: lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ")
    for tomar_cada_numero_lista in lista_numeros:
        print(f"Voy en la Iteración #{contador_iteraciones}")
        print(f"Estaremos tomando cada número de la lista: {tomar_cada_numero_lista}")
        suma_de_cada_numero_lista = suma_de_cada_numero_lista + tomar_cada_numero_lista
        print(f"La suma de la lista en la iteración #{contador_iteraciones} es de = {suma_de_cada_numero_lista}")
        contador_iteraciones = contador_iteraciones + 1
    promedio_de_suma_lista_numeros(suma_de_cada_numero_lista, contador_iteraciones)


def promedio_de_suma_lista_numeros(suma_total_lista, cantidad_numeros_lista):
	promedio = suma_total_lista/cantidad_numeros_lista
	print(f"El promedio_de_suma_lista_numeros es = {promedio}")

def filtrando_pares_de_la_lista_numeros():
    lista_pares_a_guardar = [numero for numero in lista_numeros if numero % 2 == 0]
    print(f"Lista de números pares filtrados: {lista_pares_a_guardar}")



sumar_lista_numeros()
filtrando_pares_de_la_lista_numeros()
    