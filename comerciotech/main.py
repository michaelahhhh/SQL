from clientes import *
from productos import *
from pedidos import *
while True:
    def menu_principal():
        print("<|||menu principal de comerciotech|||>")
        print("1. menu de productos")
        print("2. menu de clientes")
        print("3. menu de pedidos")
        print("4. Salir")
    input_usuario = input("Ingrese una opción: ")
    if input_usuario == "1":
        menu_productos()
        elif input_usuario == "2":
            menu_clientes()
        elif input_usuario == "3":
            menu_pedidos()
        elif input_usuario == "4":
            print("Saliendo del programa...")
            break 