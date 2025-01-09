lista = [1, 2, 3, 4, 5, 6, 7]

def sumar_lista():
    contador = 0
    aux = 0
    for numeros_de_lista in lista:
        contador += numeros_de_lista
        aux += 1
        print(f"Suma acumulada: {contador}")  # Claridad en los mensajes

    print(f"\nLa suma total de los números de la lista es: {contador}\n")
    promedio_numeros(contador, aux)  # Llamar con los parámetros correctos

def promedio_numeros(suma_total , cantidad_numeros):
    promedio = suma_total , cantidad_numeros
    print(f"El promedio de la lista de números es: {promedio}\n")

def lista_pares_encontrados():
    pares = [numero for numero in lista if numero % 2 == 0]  # Encontrar pares
    print(f"La lista de números pares encontrados es: {pares}\n")

def mostrar_resultados_anteriores():
    print("Mostrando todos los resultados anteriores:")
    sumar_lista()
    lista_pares_encontrados()

# Llamadas a las funciones
sumar_lista()
lista_pares_encontrados()
mostrar_resultados_anteriores()
