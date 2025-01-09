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
  inventario_frutas = {
   "Piña":{"Inventario": 50 ,"Precio":20},
   "Naranja":{"Inventario": 100, "Precio": 30}
  }

  def mostrar_inventario(inventario_frutas):
      for fruta in inventario_frutas:
        print(
                 f"Fruta: {fruta} - Inventario: {inventario_frutas[fruta]['Inventario']} - "
                 f"Precio por kilogramo: ${inventario_frutas[fruta]['Precio']}"
             )

  def registrar_pedido():
    pass

  def registrar_cantidades():
    pass

  def calcular_total():
    pass

  def procesar_pedido():
    pass

# Crear un objeto de tipo fruta
mi_fruta = Fruit()

# Usar (llamar) los métodos del objeto Fruta
mi_fruta.mostrar_inventario()
mi_fruta.registrar_pedido()
mi_fruta.calcular_total()
mi_fruta.procesar_pedido()
