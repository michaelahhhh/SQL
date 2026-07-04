

from bson.objectid import ObjectId
from conexion import productos as coleccion


def agregar_producto():
    try:
        cantidad = int(input("¿Cuántos productos desea ingresar? ").strip())
    except ValueError:
        cantidad = 1

    if cantidad <= 0:
        cantidad = 1

    productos_nuevos = []
    for i in range(cantidad):
        print(f"\nProducto {i + 1}")
        es_consola = input("¿Es una consola? (s/n): ").strip().lower() == "s"
        nombre = input("Nombre: ").strip()
        marca = input("Marca: ").strip()
        categoria = input("Categoría: ").strip()
        precio = float(input("Precio: ").strip() or 0)
        stock = int(input("Stock: ").strip() or 0)

        producto = {
            "Nombre": nombre,
            "Marca": marca,
            "Categoría": categoria,
            "Precio": precio,
            "Stock": stock,
        }

        if es_consola:
            almacenamiento = input("Almacenamiento: ").strip()
            color = input("Color: ").strip()
            producto["especificaciones"] = {
                "Almacenamiento": almacenamiento,
                "Color": color,
            }

        productos_nuevos.append(producto)

    if len(productos_nuevos) == 1:
        resultado = coleccion.insert_one(productos_nuevos[0])
        print(f"Producto insertado con _id {resultado.inserted_id}")
    else:
        resultado = coleccion.insert_many(productos_nuevos)
        print(f"Productos insertados con _ids {resultado.inserted_ids}")


def mostrar_productos():
    productos_guardados = list(coleccion.find())
    if not productos_guardados:
        print("No hay productos registrados en la base de datos.")
        return

    print("\nLista de productos:")
    for producto in productos_guardados:
        print("-" * 40)
        print(f"_id: {producto.get('_id')}")
        print(f"Nombre: {producto.get('Nombre')}")
        print(f"Categoría: {producto.get('Categoría')}")
        print(f"Marca: {producto.get('Marca')}")
        print(f"Precio: {producto.get('Precio')}")
        print(f"Stock: {producto.get('Stock')}")
        especificaciones = producto.get("especificaciones")
        if especificaciones:
            print("Especificaciones:")
            for clave, valor in especificaciones.items():
                print(f"  {clave}: {valor}")


def actualizar_producto():
    id_texto = input("Ingrese el _id del producto a actualizar: ").strip()
    try:
        producto_id = ObjectId(id_texto)
    except Exception:
        print("_id inválido. Debe ser un ObjectId válido.")
        return

    producto_actual = coleccion.find_one({"_id": producto_id})
    if not producto_actual:
        print("No se encontró ningún producto con ese _id.")
        return

    print("Datos actuales del producto:")
    print(f"Nombre: {producto_actual.get('Nombre')}")
    print(f"Marca: {producto_actual.get('Marca')}")
    print(f"Categoría: {producto_actual.get('Categoría')}")
    print(f"Precio: {producto_actual.get('Precio')}")
    print(f"Stock: {producto_actual.get('Stock')}")

    especificaciones = producto_actual.get("especificaciones", {})
    if especificaciones:
        print("Especificaciones actuales:")
        for clave, valor in especificaciones.items():
            print(f"  {clave}: {valor}")

    nombre = input("Nuevo nombre (Enter para mantener): ").strip()
    marca = input("Nueva marca (Enter para mantener): ").strip()
    categoria = input("Nueva categoría (Enter para mantener): ").strip()
    precio_texto = input("Nuevo precio (Enter para mantener): ").strip()
    stock_texto = input("Nuevo stock (Enter para mantener): ").strip()

    es_consola = input("¿El producto es una consola? (s/n): ").strip().lower()

    almacenamiento = ""
    color = ""

    if es_consola == "s":
        almacenamiento = input("Nuevo almacenamiento (Enter para mantener): ").strip()
        color = input("Nuevo color (Enter para mantener): ").strip()

    cambios = {}

    if nombre:
        cambios["Nombre"] = nombre

    if marca:
        cambios["Marca"] = marca

    if precio_texto:
        cambios["Precio"] = float(precio_texto)

    if stock_texto:
        cambios["Stock"] = int(stock_texto)

    if categoria:
        cambios["Categoría"] = categoria

    if es_consola == "s" and (almacenamiento or color):
        nueva_especificaciones = especificaciones.copy()

        if almacenamiento:
            nueva_especificaciones["Almacenamiento"] = almacenamiento

        if color:
            nueva_especificaciones["Color"] = color

        cambios["especificaciones"] = nueva_especificaciones

    if not cambios:
        print("No se realizaron cambios.")
        return

    resultado = coleccion.update_one(
        {"_id": producto_id},
        {"$set": cambios}
    )

    if resultado.modified_count:
        print("Producto actualizado correctamente.")
    else:
        print("No se realizaron cambios en el producto.")

def eliminar_producto():
    id_texto = input("Ingrese el _id del producto a eliminar: ").strip()
    try:
        producto_id = ObjectId(id_texto)
    except Exception:
        print("_id inválido. Debe ser un ObjectId válido.")
        return

    resultado = coleccion.delete_one({"_id": producto_id})
    if resultado.deleted_count:
        print("Producto eliminado correctamente.")
    else:
        print("No se encontró ningún producto con ese _id.")


def modificar_producto():
    actualizar_producto()
