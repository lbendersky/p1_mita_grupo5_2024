from matriz_stock import stock_menu
from ventas import ventas_menu
from cliente import clientes_menu
import validaciones
import json

def __main__():  
    intentos=0
    while True:
        try:
                if intentos==3:
                    print("El acceso al archivo ha sido denegado por la cantidad de errores que ha cometido")
                    return
                lugar_del_puesto =int(input("Seleccione que usuario ingresar: 0 cerrar programa, 1 jefe, 2 area de stock, 3 area de clientes, 4 area de ventas: "))
                if lugar_del_puesto == 0:
                    print("Cerrando programa...")
                    return
                elif 0<lugar_del_puesto<5:
                    contra = input("Ingrese la contraseña o ingrese 0 para regresar: ")
                    if contra == "0":
                        continue
                    usuario = validaciones.login(contra, lugar_del_puesto)
                    break
                
                else:
                    print("Por favor ingrese un valor valido.")
                    intentos+=1 
                    continue
                
        except:
            intentos+=1 
            print("Dato no valido.")

    matriz_stock = []
    matriz_ventas=[]
    matriz_clientes= []

    try:
        with open(r"p1_mita_grupo5_2024\archivos_csv\clientes.txt","r",encoding="UTF-8") as archivo_cliente:
            for linea in archivo_cliente:
                linea = linea.strip()
                if linea=="":
                    break
                idcliente,nombrecliente,numerocliente,correocliente = linea.split(";")
                partes= linea.split(";")
                if len(partes)!=4:
                    break
                matriz_clientes.append([])

                matriz_clientes[len(matriz_clientes)-1].append(int(idcliente))
                matriz_clientes[len(matriz_clientes)-1].append(nombrecliente)
                matriz_clientes[len(matriz_clientes)-1].append(numerocliente)
                matriz_clientes[len(matriz_clientes)-1].append(correocliente)

    except FileNotFoundError:
        print("El archivo 'clientes.txt' no fue encontrado")
    except OSError:
        print("Ha sucedido un error con el archivo 'clientes.txt'")


    try:
        with open(r"p1_mita_grupo5_2024\archivos_csv\productos.txt","r",encoding="UTF-8") as archivo_producto:
            for linea in archivo_producto:
                linea = linea.strip()
                if linea=="":
                    break
                idproducto,nombreproducto,cantidad=linea.split(";")
                partes=linea.split(";")
                if len(partes)!=3:
                    break
                matriz_stock.append([])

                matriz_stock[len(matriz_stock)-1].append(int(idproducto))
                matriz_stock[len(matriz_stock)-1].append(nombreproducto)
                matriz_stock[len(matriz_stock)-1].append(int(cantidad))
    
    except FileNotFoundError:
        print("El archivo 'productos.txt' no fue encontrado")
    except OSError:
        print("Ha sucedido un error con el archivo 'productos.txt'")
       
        
    try:
        with open(r"p1_mita_grupo5_2024\archivos_csv\ventas.json","r",encoding="UTF-8") as archivo_ventas:
            matriz_ventas=json.load(archivo_ventas)
    except FileNotFoundError:
        print("El archivo 'ventas.json' no fue encontrado")
    except OSError:
        print("Ha sucedido un error con el archivo 'ventas.json'")
            
    print()
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