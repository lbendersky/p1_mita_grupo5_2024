from matriz_stock import stock_menu
from ventas import ventas_menu
from cliente import clientes_menu
import validaciones


def __main__():  
    
    while True:
        try:
                lugar_del_puesto = int(input("Seleccione que usuario ingresar: 1 jefe, 2 area de stock, 3 area de clientes, 4 area de ventas: "))
                contra = input("Ingrese la contraseña: ")
                usuario = validaciones.login(contra, lugar_del_puesto)
                break
        except:
            print("Datos no validos")

    matriz_stock = []
    matriz_ventas=[]
    matriz_clientes= []

    flag = 0
    while flag == 0:
        qmatriz = input("Ingrese la matriz que desea modificar o visualizar: 1 stock, 2 clientes, 3 ventas, 4 frenar el proceso: ")
        
        if validaciones.vnumero(qmatriz):
        
            qmatriz=int(qmatriz)
            if qmatriz == 1 and usuario["stock"] == 1:
                stock_menu(matriz_stock)
            elif qmatriz == 2 and usuario["clientes"] == 1:
                clientes_menu(matriz_clientes)
            elif qmatriz == 3 and usuario["ventas"] == 1:
                ventas_menu(matriz_ventas,matriz_clientes,matriz_stock)
            elif qmatriz == 4:
                flag = 1
            else:
                print("Ingrese un numero correcto")


if __name__ == __main__():
    __main__()