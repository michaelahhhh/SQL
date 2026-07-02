from cliente import *
from productos import *
from pedidos import *


def menu_productos():
    while True:
        print("\n<||| MENÚ PRODUCTOS |||>")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Volver")

        opcion = input("Ingrese opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            modificar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            break
        else:
            print("Opción inválida")


def menu_clientes():
    while True:
        print("\n<||| MENÚ CLIENTES |||>")
        print("1. Agregar cliente")
        print("2. Mostrar clientes")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("5. Volver")

        opcion = input("Ingrese opción: ")

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            mostrar_clientes()
        elif opcion == "3":
            modificar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            break
        else:
            print("Opción inválida")


def menu_pedidos():
    while True:
        print("\n<||| MENÚ PEDIDOS |||>")
        print("1. Agregar pedido")
        print("2. Mostrar pedidos")
        print("3. Modificar pedido")
        print("4. Eliminar pedido")
        print("5. Volver")

        opcion = input("Ingrese opción: ")

        if opcion == "1":
            agregar_pedido()
        elif opcion == "2":
            mostrar_pedidos()
        elif opcion == "3":
            modificar_pedido()
        elif opcion == "4":
            eliminar_pedido()
        elif opcion == "5":
            break
        else:
            print("Opción inválida")


def menu_principal():
    while True:
        print("\n<||| MENÚ PRINCIPAL COMERCIOTECH |||>")
        print("1. Menú productos")
        print("2. Menú clientes")
        print("3. Menú pedidos")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            menu_productos()
        elif opcion == "2":
            menu_clientes()
        elif opcion == "3":
            menu_pedidos()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida")



menu_principal()
