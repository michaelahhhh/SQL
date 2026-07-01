from comerciotech import cliente
from conexion import productos

def agregar_producto():

db = cliente['comercioTech']
coleccion = db ['Catalogo_Producto']

ListaConsolas = []

c = int(input("¿Cuantos Productos Quiere Ingresar?: "))
if c == 1:
    print("¿Es Una Consola?")
    print("1.- Si")
    print("2.- No")
    t = int(input(""))
    if t == 1:
        Nombre = input("Cual es el Nombre: ")
        Marca = input("Cual es la Marca: ")
        Precio = float(input("Cual es el Precio: "))
        Stock = int(input("Cual es el Stock: "))
        Almacenamiento = input("Cuanto de Almacenamiento tiene: ")
        Color = input("Cual es el Color: ")
        

        Consola = {
            "Nombre": Nombre,
            "Marca": Marca,
            "Precio": Precio,
            "Stock": Stock,
            "especificaciones": {
                "Almacenamiento": Almacenamiento,
                "color": Color
            }}
        resultado = coleccion.insert_one(Consola)
        print(f"Producto insertado con _id {resultado.inserted_id}")
    elif t == 2:
        Nombre = input("Cual es el Nombre: ")
        Marca = input("Cual es la Marca: ")
        Precio = float(input("Cual es el Precio: "))
        Stock = int(input("Cual es el Stock: "))
        

        Consola = {
            "Nombre": Nombre,
            "Marca": Marca,
            "Precio": Precio,
            "Stock": Stock}
        resultado = coleccion.insert_one(Consola)
        print(f"Producto Insertado Con _ID{resultado.inserted_id}")


else:
    while c >= 1:
        print("¿Es Una Consola?")
        print("1.- Si")
        print("2.- No")
        t = int(input(""))
        if t == 1:
            Nombre = input("Cual es el Nombre: ")
            Marca = input("Cual es la Marca: ")
            Precio = float(input("Cual es el Precio: "))
            Stock = int(input("Cual es el Stock: "))
            Almacenamiento = input("Cuanto de Almacenamiento tiene: ")
            Color = input("Cual es el Color: ")
    
        
            Consola = {
                "Nombre": Nombre,
                "Marca": Marca,
                "Precio": Precio,
                "Stock": Stock,
                "especificaciones": {
                    "Almacenamiento": Almacenamiento,
                    "color": Color
                }
                }
        elif t == 2:
            Nombre = input("Cual es el Nombre: ")
            Marca = input("Cual es la Marca: ")
            Precio = float(input("Cual es el Precio: "))
            Stock = int(input("Cual es el Stock: "))
            Consola = {
                 
                "Nombre": Nombre,
                "Marca": Marca,
                "Precio": Precio,
                "Stock": Stock}
            
        ListaConsolas.append(Consola)
        c = c-1

    resultado = coleccion.insert_many(ListaConsolas)
    print(f"Producto insertado con _id {resultado.inserted_ids}")