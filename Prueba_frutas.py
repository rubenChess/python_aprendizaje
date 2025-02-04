# Paso 1: Mostrar el inventario
def mostrar_inventario(inventario):
    print("\n*** Inventario de Frutas ***")
    for fruta, precio in inventario.items():
        print(f"{fruta}: ${precio:.2f} por kilogramo")
    print("\n")  # Línea en blanco para mejor presentación

# Paso 2: Registrar el pedido del cliente
def registrar_pedido(inventario):
    print("Por favor, selecciona las frutas que deseas comprar.")
    print("Escribe el nombre de la fruta o 'salir' para terminar.")
    
    frutas_seleccionadas = []
    while True:
        fruta = input("Fruta: ").strip().lower()
        if fruta == "salir":
            break
        if fruta in inventario:
            frutas_seleccionadas.append(fruta)
        else:
            print("Lo siento, esa fruta no está disponible.")
    return frutas_seleccionadas

# Paso 3: Registrar las cantidades de cada fruta seleccionada
def registrar_cantidades(frutas_seleccionadas, inventario):
    cantidades = {}
    for fruta in frutas_seleccionadas:
        while True:
            try:
                cantidad = float(input(f"¿Cuántos kilogramos de {fruta} deseas? "))
                if cantidad > 0:
                    cantidades[fruta] = cantidad
                    break
                else:
                    print("La cantidad debe ser mayor a 0.")
            except ValueError:
                print("Por favor, ingresa un número válido.")
    return cantidades

# Paso 4: Calcular el costo total
def calcular_total(cantidades, inventario):
    total = 0
    resumen = "\n*** Resumen del Pedido ***\n"
    for fruta, cantidad in cantidades.items():
        precio = inventario[fruta]
        costo = precio * cantidad
        total += costo
        resumen += f"{fruta.capitalize()}: {cantidad} kg x ${precio:.2f}/kg = ${costo:.2f}\n"
    resumen += f"\nTotal a pagar: ${total:.2f}"
    return total, resumen

# Paso 5: Integrar todo en una función procesar_pedido
def procesar_pedido():
    # Definir el inventario de frutas (nombre y precio por kilogramo)
    inventario = {
        "manzana": 3.5,
        "platano": 2.0,
        "naranja": 4.0,
        "pera": 3.8,
        "uva": 6.0
    }
    
    # Mostrar el inventario
    mostrar_inventario(inventario)
    
    # Registrar el pedido del cliente
    frutas_seleccionadas = registrar_pedido(inventario)
    if not frutas_seleccionadas:
        print("No seleccionaste ninguna fruta. ¡Gracias por visitarnos!")
        return
    
    # Registrar las cantidades de cada fruta seleccionada
    cantidades = registrar_cantidades(frutas_seleccionadas, inventario)
    
    # Calcular el costo total y mostrar el resumen
    total, resumen = calcular_total(cantidades, inventario)
    print(resumen)

# Ejecutar el programa
if __name__ == "__main__":
    procesar_pedido()
