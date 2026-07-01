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


    def menu_productos():
        print("<|||menu de productos|||>")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Volver al menú principal")


        if input_usuario == "1":
            agregar_producto()
        elif input_usuario == "2":
            mostrar_productos()
        elif input_usuario == "3":
            modificar_producto()
        elif input_usuario == "4":
            eliminar_producto()
        elif input_usuario == "5":
            menu_principal()


    def menu_clientes():
        print("<|||menu de clientes|||>")
        print("1. Agregar cliente")
        print("2. Mostrar clientes")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("5. Volver al menú principal")


        if input_usuario == "1":
            agregar_cliente()
        elif input_usuario == "2":
            mostrar_clientes()
        elif input_usuario == "3":
            modificar_cliente()
        elif input_usuario == "4":
            eliminar_cliente()
        elif input_usuario == "5":
            menu_principal()

    def menu_pedidos():
        print("<|||menu de pedidos|||>")
        print("1. Agregar pedido")
        print("2. Mostrar pedidos")
        print("3. Modificar pedido")
        print("4. Eliminar pedido")
        print("5. Volver al menú principal")

        if input_usuario == "1":
            agregar_pedido()
        elif input_usuario == "2":
            mostrar_pedidos()
        elif input_usuario == "3":  
            modificar_pedido()
        elif input_usuario == "4":
            eliminar_pedido()
        elif input_usuario == "5":
            menu_principal()