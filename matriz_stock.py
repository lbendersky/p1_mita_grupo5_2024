from funciones import crear_stock, leer, actualizarstock, destruir, organizar_stock

matriz_stock = []

def stock_menu():
    num = int(input("seleccione una opcion: 1 crear, 2 leer, 3 actualizar, 4 eliminar, 5 volver al principio: "))

    if num == 1:
        prod = input("Nombre del producto: ")
        cant = int(input("Cantidad del producto: "))
        crear_stock(matriz_stock, prod, cant)
        stock_menu()
    elif num == 2:
        leer(matriz_stock, stock=1)
        stock_menu()
    elif num == 3:
        pos=int(input("Ingrese el ID del stock que desea actualizar"))

        print("Tenga en cuenta lo siguiente: ")
        print("1- Nombre")
        print("2- Cantidad")
        print("3- Precio de Compra")
        print("4- Precio de Venta")

        opciones=int(input("Ingrese el valor a cambiar: "))
        objeto=int(input("Ingrese el valor por el que lo va a cambiar"))

        actualizarstock(matriz_stock, pos, opciones, objeto)
        stock_menu()
    elif num == 4:
        destruir(matriz_stock)
        stock_menu()
    else:
        return