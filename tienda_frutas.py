"""
Ejercicio: Tienda de Frutas
Vas a escribir un programa que simule la gestión de un pedido en una tienda
de frutas. El programa debe:

Mostrar el inventario de frutas disponible.
Permitir al cliente seleccionar las frutas que desea comprar.
Registrar las cantidades de cada fruta seleccionada.
Calcular el costo total de la compra.
Mostrar un resumen detallado del pedido al cliente.

Paso a paso
1. Crear una función llamada mostrar_inventario
  - Recibe un diccionario con el inventario de frutas (nombre y precio por
    kilogramo) como argumento.
  - Muestra al usuario las frutas disponibles y sus precios.
2. Crear una función llamada registrar_pedido
  - Recibe un diccionario con el inventario de frutas.
  - Permite al cliente seleccionar las frutas que desea comprar.
  - Devuelve una lista de las frutas seleccionadas por el cliente.
3. Crear una función llamada registrar_cantidades
  - Recibe una lista de frutas seleccionadas y el inventario como argumentos.
  - Pide al cliente la cantidad (en kilogramos) de cada fruta seleccionada.
  - Devuelve un diccionario con las frutas y sus cantidades.
4. Crear una función llamada calcular_total
  - Recibe un diccionario con las frutas seleccionadas y sus cantidades, además
    del inventario.
  - Calcula el precio total de la compra.
  - Devuelve el total y un resumen detallado del pedido.
5. Crear una función llamada procesar_pedido
  - Integra todas las funciones anteriores.
  - Muestra el inventario, permite registrar el pedido, calcula el total y muestra
    un resumen.
"""
# Definimos una clase para representar una fruta
# Definimos una clase para representar una fruta
class Fruta:
    def __init__(self, nombre, color, precio_por_kg):
        self.nombre = nombre
        self.color = color
        self.precio_por_kg = precio_por_kg  # Precio en la moneda local por kilogramo

    def __str__(self):
        return f"Fruta({self.nombre}, Color: {self.color}, Precio: {self.precio_por_kg} por kg)"

# Crear instancias de frutas
manzana = Fruta("Manzana", "Rojo", 3.5)
banana = Fruta("Banana", "Amarillo", 2.8)
naranja = Fruta("Naranja", "Naranja", 3.2)
pera = Fruta("Pera", "Verde", 3.0)

# Crear un diccionario con las frutas
diccionario_frutas = {
    "manzana": manzana,
    "banana": banana,
    "naranja": naranja,
    "pera": pera
}

# Mostrar el diccionario de frutas
for clave, fruta in diccionario_frutas.items():
    print(f"{clave.capitalize()}: {fruta}")
