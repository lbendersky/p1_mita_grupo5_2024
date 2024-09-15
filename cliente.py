
from funciones import crear_clientes, leer, actualizarcliente, destruir

matriz_clientes=[]

def clientes_menu():
    num = int(input("seleccione una opcion: 1 crear, 2 leer, 3 actualizar, 4 eliminar, 5 volver al principio: "))

    if num == 1:
        nomb = input("Nombre del cliente: ")
        tel = int(input("Ingrese el número del cliente: "))
        corr = input("Ingrese el correo electronico: ")
        
        crear_clientes(matriz_clientes, nomb, tel, corr)
        clientes_menu()
    elif num == 2:
        leer(matriz_clientes, stock=1)
        clientes_menu()
    elif num == 3:
        pos=int(input("Ingrese el ID del stock que desea actualizar"))

        print("Tenga en cuenta lo siguiente: ")
        print("1- Nombre")
        print("2- Cantidad")
        print("3- Precio de Compra")
        print("4- Precio de Venta")

        opciones=int(input("Ingrese el valor a cambiar: "))
        objeto=int(input("Ingrese el valor por el que lo va a cambiar"))

        actualizarcliente(matriz_clientes, pos, opciones, objeto)
        clientes_menu()
    elif num == 4:
        pos = int(input("Ingrese el ID de cliente que desea eliminar: "))

        destruir(matriz_clientes, pos)
        clientes_menu()
    else:
        return
