from conexion import clientes

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
