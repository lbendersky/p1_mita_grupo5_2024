from matriz_stock import stock_menu
from ventas import ventas_menu
from cliente import clientes_menu
import validaciones
import sys

def __main__():  
    
    while True:
        try:
                lugar_del_puesto =int(input("Seleccione que usuario ingresar: 0 cerrar programa, 1 jefe, 2 area de stock, 3 area de clientes, 4 area de ventas: "))
                if lugar_del_puesto == 0:
                    print("cerrando programa...")
                    return
                elif lugar_del_puesto<5 and lugar_del_puesto>0:
                    contra = input("Ingrese la contraseña o ingrese 0 para regresar: ")
                    if contra == "0":
                        continue
                    usuario = validaciones.login(contra, lugar_del_puesto)
                    break
                else:
                    print("Por favor ingrese un valor valido.")
                    continue
                
        except:
            print("Dato no valido.", sys.exc_info())

    matriz_stock = []
    matriz_ventas=[]
    matriz_clientes= []

    try:
        with open(r"C:\Users\retro\Python VSC\TrabajoGrupal\archivos_csv\clientes.txt","r",encoding="UTF-8") as archivo_cliente:
            for linea in archivo_cliente:
                linea = linea.strip()
                if linea=="":
                    break
                idcliente,nombrecliente,numerocliente,correocliente = linea.split(";")
                partes= linea.split(";")
                if len(partes)!=4:
                    break
                matriz_clientes.append([])

                matriz_clientes[len(matriz_clientes)-1].append(idcliente)
                matriz_clientes[len(matriz_clientes)-1].append(nombrecliente)
                matriz_clientes[len(matriz_clientes)-1].append(numerocliente)
                matriz_clientes[len(matriz_clientes)-1].append(correocliente)

    except:
        print("Ha sucedido un error inesperado")

    try:
        with open(r"C:\Users\retro\Python VSC\TrabajoGrupal\archivos_csv\productos.txt","r",encoding="UTF-8") as archivo_producto:
            for linea in archivo_producto:
                linea = linea.strip()
                if linea=="":
                    break
                idproducto,nombreproducto,cantidad=linea.split(";")
                partes=linea.split(";")
                if len(partes)!=3:
                    break
                matriz_stock.append([])

                matriz_stock[len(matriz_stock)-1].append(idproducto)
                matriz_stock[len(matriz_stock)-1].append(nombreproducto)
                matriz_stock[len(matriz_stock)-1].append(cantidad)
    
    except:
        print("Ha ocurrido un error inesperado.")

    while True:
        
        qmatriz = int(input("Ingrese la matriz que desea modificar o visualizar: 1 stock, 2 clientes, 3 ventas, 4 frenar el proceso: "))
        
        if validaciones.vnumero(qmatriz):
        
            qmatriz=int(qmatriz)
            if qmatriz == 1 and usuario["stock"] == 1:
                stock_menu(matriz_stock)
            elif qmatriz == 2 and usuario["clientes"] == 1:
                clientes_menu(matriz_clientes)
            elif qmatriz == 3 and usuario["ventas"] == 1:
                ventas_menu(matriz_ventas,matriz_clientes,matriz_stock)
            elif qmatriz == 4:
                break
            else:
                print("Ingrese un numero correcto")
                continue


if __name__ == __main__():
    __main__()