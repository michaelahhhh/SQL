from bson import ObjectId

from conexion import pedidos
from pymongo import MongoClient

MongoClient = MongoClient("mongodb://localhost:27017/")
db = MongoClient["comerciotech"]
coleccion = db["pedidos"]

def agregar_pedido():
    print("Ingrese los datos del pedido:")
    cliente_id = input("ID del cliente: ")
    producto_id = input("ID del producto: ")
    cantidad = int(input("Cantidad: "))
    fecha = input("Fecha (YYYY-MM-DD): ")

    pedido = {
        "cliente_id": cliente_id,
        "producto_id": producto_id,
        "cantidad": cantidad,
        "fecha": fecha
    }

    resultado = coleccion.insert_one(pedido)
    print(f"Pedido insertado con _id {resultado.inserted_id}")
def mostrar_pedidos():
    print("\nLista de pedidos:")
    pedidos_guardados = list(coleccion.find())

    if not pedidos_guardados:
        print("No hay pedidos registrados en la base de datos.")
        return

    for pedido in pedidos_guardados:
        print("-" * 40)
        print(f"_id: {pedido.get('_id')}")
        print(f"ID del cliente: {pedido.get('cliente_id')}")
        print(f"ID del producto: {pedido.get('producto_id')}")
        print(f"Cantidad: {pedido.get('cantidad')}")
        print(f"Fecha: {pedido.get('fecha')}")

def modificar_pedido():
    pedido_id = input("Ingrese el _id del pedido a modificar: ")
    pedido = coleccion.find_one({"_id": ObjectId(pedido_id)})

    if not pedido:
        print("Pedido no encontrado.")
        return

    print("Ingrese los nuevos datos del pedido (deje en blanco para mantener el valor actual):")
    cliente_id = input(f"ID del cliente ({pedido['cliente_id']}): ") or pedido['cliente_id']
    producto_id = input(f"ID del producto ({pedido['producto_id']}): ") or pedido['producto_id']
    cantidad = input(f"Cantidad ({pedido['cantidad']}): ") or pedido['cantidad']
    fecha = input(f"Fecha ({pedido['fecha']}): ") or pedido['fecha']

    pedido_actualizado = {
        "cliente_id": cliente_id,
        "producto_id": producto_id,
        "cantidad": cantidad,
        "fecha": fecha
    }

    coleccion.update_one({"_id": ObjectId(pedido_id)}, {"$set": pedido_actualizado})
    print("Pedido actualizado correctamente.")

def eliminar_pedido():
    pedido_id = input("Ingrese el _id del pedido a eliminar: ")
    resultado = coleccion.delete_one({"_id": ObjectId(pedido_id)})

    if resultado.deleted_count > 0:
        print("Pedido eliminado correctamente.")
    else:
        print("No se encontró ningún pedido con ese _id.")
