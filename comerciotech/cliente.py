from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client["comerciotech"]
coleccion = db["clientes"]


def agregar_cliente():
    print("\n--- AGREGAR CLIENTE ---")

    nombre = input("Nombre: ")
    email = input("Email: ")
    telefono = input("Teléfono: ")

    cliente = {
        "nombre": nombre,
        "email": email,
        "telefono": telefono
    }

    resultado = coleccion.insert_one(cliente)
    print(f"\nCliente agregado correctamente.")
    print(f"ID generado: {resultado.inserted_id}")


def mostrar_clientes():
    print("\n--- LISTA DE CLIENTES ---")

    clientes = list(coleccion.find())

    if len(clientes) == 0:
        print("No hay clientes registrados.")
        return

    for cliente in clientes:
        print(f"""
ID: {cliente['_id']}
Nombre: {cliente['nombre']}
Email: {cliente['email']}
Teléfono: {cliente['telefono']}
-----------------------------------
""")


def modificar_cliente():
    print("\n--- MODIFICAR CLIENTE ---")

    cliente_id = input("Ingrese el ID del cliente: ")

    try:
        cliente = coleccion.find_one({"_id": ObjectId(cliente_id)})
    except:
        print("ID inválido.")
        return

    if cliente is None:
        print("Cliente no encontrado.")
        return

    nombre = input(f"Nombre ({cliente['nombre']}): ")
    email = input(f"Email ({cliente['email']}): ")
    telefono = input(f"Teléfono ({cliente['telefono']}): ")

    datos_actualizados = {
        "nombre": nombre if nombre else cliente["nombre"],
        "email": email if email else cliente["email"],
        "telefono": telefono if telefono else cliente["telefono"]
    }

    coleccion.update_one(
        {"_id": ObjectId(cliente_id)},
        {"$set": datos_actualizados}
    )

    print("Cliente actualizado correctamente.")


def eliminar_cliente():
    print("\n--- ELIMINAR CLIENTE ---")

    cliente_id = input("Ingrese el ID del cliente: ")

    try:
        resultado = coleccion.delete_one({"_id": ObjectId(cliente_id)})
    except:
        print("ID inválido.")
        return

    if resultado.deleted_count > 0:
        print("Cliente eliminado correctamente.")
    else:
        print("Cliente no encontrado.")
