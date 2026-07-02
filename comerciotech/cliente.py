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

def mostrar_clientes():
    hay=False
    for c in coleccion.find():
        hay=True
        print(c)
    if not hay: print("Sin clientes")
