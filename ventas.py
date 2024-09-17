import funciones
import validaciones

def ventas_menu(matriz_ventas,matriz_clientes,matriz_stock):
    flag = 0
    while flag==0:
        num=input("Tenga en cuenta lo siguiente:\n1- Crear \n2- Leer \n3- Actualizar \n4- Borrar archivo \n5- Volver al menu \n\nIngrese lo que desea hacer: ")

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
                                print("El correo o el nombre del producto estan mal escritos o no existen")
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
                    print("Tenga en cuenta lo siguiente: \n1- Nombre del comprador \n2- Cantidad vendida \n3- Fecha")

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
                    else:
                        print("El número ingresado es incorrecto")
                        
                matriz_ventas=funciones.actualizarventas(matriz_ventas,pos,opcion,datoacambiar)
            elif num==4: 
                band=0
                while band==0:
                    pos=input("Ingrese el ID que desea eliminar: ")
                    if validaciones.vnumero(pos):
                        pos=int(pos)
                        if validaciones.vidmatriz(matriz_clientes,pos):
                            band=1
                funciones.destruir(matriz_ventas,pos)
            elif num==5:
                flag = 1
                return
            else:
                print("\nIngrese un numero correcto\n")