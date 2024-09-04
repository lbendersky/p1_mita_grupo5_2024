from matriz_stock import stock_menu
from ventas import ventas_menu
from clientes import clientes_menu



def __main__():
    qmatriz = int(input("Ingrese la matriz que desea modificar o visualizar: 1 stock, 2 clientes, 3 ventas: "))

    if qmatriz == 1:
        stock.menu()
    elif qmatriz == 2:
        clientes.menu()
    elif qmatriz == 3:
        ventas.menu()
    else:
        __main__()

if __name__ == __main__():
    __main__()