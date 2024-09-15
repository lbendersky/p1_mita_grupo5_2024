from matriz_stock import stock_menu
from ventas import ventas_menu
from cliente import clientes_menu

matriz_stock = []
matriz_ventas=[]

def __main__():
    qmatriz = int(input("Ingrese la matriz que desea modificar o visualizar: 1 stock, 2 clientes, 3 ventas, 4 frenar el proceso: "))

    if qmatriz == 1:
        stock_menu(matriz_stock)
    elif qmatriz == 2:
        clientes_menu()
    elif qmatriz == 3:
        ventas_menu(matriz_ventas)
    elif qmatriz == 4:
        return
    else:
        __main__()
    __main__()


if __name__ == __main__():
    __main__()