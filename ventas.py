import funciones
import validaciones

def ventas_menu(matriz_ventas,matriz_clientes,matriz_stock):
    flag = 0
    while flag==0:
        print("Tenga en cuenta lo siguiente:")
        print("1- Crear")
        print("2- Leer")
        print("3- Actualizar")
        print("4- Borrar archivo")
        print("Ingrese cualquier otro número para salir")

        num=input("Ingrese lo que desea hacer: ")
        if validaciones.vnumero(num):
            num=int(num)
            if num==1:
                correo=input("Ingrese el correo del Usuario: ")
                if validaciones.vcorreo(correo):
                    producto=input("Ingrese el nombre del objeto: ")
                    cantidad=input("Ingrese la cantidad vendida: ")
                    if validaciones.vnumero(cantidad):
                        fechas=input("Ingrese la fecha con formato DD/MM/AAAA: ")
                        if validaciones.vfecha(fechas):
                            x=funciones.crear_ventas(matriz_stock,matriz_clientes,matriz_ventas,producto,correo,cantidad,fechas)
                            if x==1:
                                print("El correo o el nombre del producto estan mal escritos")
            elif num==2:
                funciones.leer(matriz_ventas, ventas=1)
            elif num==3:
                band=0
                while band==0:
                    pos=input("Ingrese el ID que desea actualizar: ")
                    if validaciones.vnumero(pos):
                        pos=int(pos)
                        if validaciones.vidmatriz(matriz_clientes,pos):
                            band=1
                band=0
                while band==0:
                    print("Tenga en cuenta lo siguiente: ")
                    print("1- Nombre del Comprador")
                    print("2- Cantidad Vendida")
                    print("3- Fecha")
                    while band==0:
                        opcion=input("Ingrese una opción: ")
                        if validaciones.vnumero(opcion):
                            opcion=int(opcion)
                            band=1
                        else:
                            print("No ingresado numero.")
                    if opcion==1:
                        band=0
                        while band==0:
                            datoacambiar=input("Ingrese el dato por el que desea cambiarlo: ")
                            if validaciones.vtexto(datoacambiar):
                                band+=1
                    elif opcion==2:
                        band=0
                        while band==0:
                            datoacambiar=input("Ingrese el dato por el que desea cambiarlo: ")
                            if validaciones.vnumero(datoacambiar):
                                band+=1
                    elif opcion==3:
                        band=0
                        while band==0:
                            datoacambiar=input("Ingrese el dato por el que desea cambiarlo: ")
                            if validaciones.vfecha(datoacambiar):
                                band=1
                    elif opcion==5:
                        band=1
                    else:
                        print("El número ingresado es incorrecto")
                matriz_ventas=funciones.actualizarventas(matriz_ventas,pos,opcion,datoacambiar)
                ventas_menu(matriz_ventas,matriz_clientes,matriz_stock)
            elif num==4: 
                band=0
                while band==0:
                    pos=input("Ingrese el ID que desea eliminar: ")
                    if validaciones.vnumero(pos):
                        if validaciones.vidmatriz(matriz_clientes,pos):
                            band=1
                funciones.destruir(matriz_ventas,pos)
                matriz_clientes=ventas_menu(matriz_ventas,matriz_clientes,matriz_stock)
            else:
                return