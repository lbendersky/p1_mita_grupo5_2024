from funciones import crear_stock, leer, actualizarstock, destruir


def stock_menu(matriz_stock):
    num = int(input("seleccione una opcion: 1 crear, 2 leer, 3 actualizar, 4 eliminar, 5 volver al principio: "))

    if num == 1:
        prod = input("Nombre del producto: ")
        cant = int(input("Cantidad del producto: "))
        matriz_stock = crear_stock(matriz_stock, prod, cant)
        stock_menu(matriz_stock)
    elif num == 2:
        leer(matriz_stock, stock=1)
        stock_menu(matriz_stock)
    elif num == 3:
        pos=int(input("Ingrese el ID del stock que desea actualizar"))

        print("Tenga en cuenta lo siguiente: ")
        print("1- Nombre")
        print("2- Cantidad")

        opciones=int(input("Ingrese el valor a cambiar: "))

        if opciones==1:
            objeto = input("Ingrese nombre del producto: ")
        elif opciones==2:
            objeto = int(input("Ingrese cantidad del producto: "))
        else:
            print("El número ingresado es incorrecto")

        matriz_stock = actualizarstock(matriz_stock, pos, opciones, objeto)
        stock_menu(matriz_stock)
    elif num == 4:
        pos = int(input("Ingrese el ID del producto que desea eliminar: "))

        destruir(matriz_stock, pos)
        matriz_stock = stock_menu(matriz_stock)
    else:
        return