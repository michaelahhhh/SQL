from http import client
from conexion import clientes
from pymongo import MongoClient
from bson.objectid import ObjectId

MongoClient = MongoClient("mongodb://localhost:27017/")
db = MongoClient["comerciotech"]
coleccion = db["clientes"]

def agregar_cliente():

    print("Ingrese los datos del cliente:")
    nombre = input("Nombre: ")
    Correo = input("Email: ")
    telefono = input("Teléfono: ")

    cliente = {
        "nombre": nombre,
        "email": Correo,
        "telefono": telefono
    }

    resultado = coleccion.insert_one(cliente)
    print(f"Cliente insertado con _id {resultado.inserted_id}")

def mostrar_clientes():

    print ("\nLista de clientes:")
    clientes_guardados = list(coleccion.find())

    if not clientes_guardados:
        print("No hay clientes registrados en la base de datos.")
        return
        
def modificar_cliente():
    cliente_id = input("Ingrese el _id del cliente a modificar: ")
    cliente = coleccion.find_one({"_id": ObjectId(cliente_id)})

    if not cliente:
        print("Cliente no encontrado.")
        return

    print("Ingrese los nuevos datos del cliente (deje en blanco para mantener el valor actual):")
    nombre = input(f"Nombre ({cliente['nombre']}): ") or cliente['nombre']
    email = input(f"Email ({cliente['email']}): ") or cliente['email']
    telefono = input(f"Teléfono ({cliente['telefono']}): ") or cliente['telefono']

    cliente_actualizado = {
        "nombre": nombre,
        "email": email,
        "telefono": telefono
    }

    coleccion.update_one({"_id": ObjectId(cliente_id)}, {"$set": cliente_actualizado})
    print("Cliente actualizado correctamente.")

def eliminar_cliente():
    cliente_id = input("Ingrese el _id del cliente a eliminar: ")
    resultado = coleccion.delete_one({"_id": ObjectId(cliente_id)})

    if resultado.deleted_count > 0:
        print("Cliente eliminado correctamente.")
    else:
        print("No se encontró ningún cliente con ese _id.")
