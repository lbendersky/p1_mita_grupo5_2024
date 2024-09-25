from matriz_stock import stock_menu
from ventas import ventas_menu
from cliente import clientes_menu
import validaciones
#1,"Zapallo",4
matriz_stock = [1,"Zapallo",4]
matriz_ventas=[]
matriz_clientes= []
#1,"Seb Sol","5491136563081","seba@mail.com"
def __main__(): 
    
    qmatriz = input("Ingrese la matriz que desea modificar o visualizar: 1 stock, 2 clientes, 3 ventas, 4 frenar el proceso: ")
    
    if validaciones.vnumero(qmatriz):
    
        qmatriz=int(qmatriz)
        if qmatriz == 1:
            stock_menu(matriz_stock)
        elif qmatriz == 2:
            clientes_menu(matriz_clientes)
        elif qmatriz == 3:
            ventas_menu(matriz_ventas,matriz_clientes,matriz_stock)
        elif qmatriz == 4:
            return
        else:
            print("Ingrese un numero correcto")
            __main__()
        __main__()
    else:
        __main__()

if __name__ == __main__():
    __main__()