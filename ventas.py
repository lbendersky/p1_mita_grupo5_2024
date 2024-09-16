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

        num=int(input("Ingrese lo que desea hacer: "))
        if num.isnumeric():
            if num==1:
                correo=input("Ingrese el correo del Usuario: ")
                if validaciones.vcorreo(correo):
                    producto=input("Ingrese el nombre del objeto: ")
                    producto.capitalize()
                    cantidad=input("Ingrese la cantidad vendida: ")
                    if validaciones.vnumero(cantidad):
                        fecha=input("Ingrese la fecha con formato DD-MM-AAAA: ")
                        if validaciones.vfecha(fecha):
                            x=funciones.crear_ventas(matriz_stock,matriz_clientes,matriz_ventas,producto,correo,fecha)
                            ventas_menu(matriz_ventas)

                            if x==1:
                                print("El correo o el nombre del producto estan mal escritos")
            elif num==2:
                funciones.leer(matriz_ventas, ventas=1)
                ventas_menu(matriz_ventas)
            elif num==3:
                a=0
                while a==0:
                    funciones.leer(matriz_ventas)
                    pos=int(input("Ingrese el ID del stock que desea actualizar: "))

                    print("Tenga en cuenta lo siguiente: ")
                    print("1- Nombre del Producto")
                    print("2- Cantidad Vendida")
                    print("3- Correo del cliente")
                    print("4- Fecha")

                    opcion=input("Ingrese una opción: ")
                    if validaciones.vnumero(opcion):
                        if opcion==1:
                            datoacambiar=input("Ingrese el dato por el que desea cambiarlo: ")
                            if validaciones.vtexto(datoacambiar):
                                x=funciones.actualizarventas(matriz_ventas,pos,opcion,datoacambiar)
                                if x!=1:
                                    a+=1
                                    ventas_menu(matriz_ventas)
                        elif opcion==2:
                            datoacambiar=input("Ingrese el dato por el que desea cambiarlo: ")
                            if validaciones.vnumero(datoacambiar):
                                x=funciones.actualizarventas(matriz_ventas,pos,opcion,datoacambiar)
                                if x!=1:
                                    a+=1
                                    ventas_menu(matriz_ventas)
                        elif opcion==3:
                            datoacambiar=input("Ingrese el dato por el que desea cambiarlo: ")
                            if validaciones.vcorreo(datoacambiar):
                                x=funciones.actualizarventas(matriz_ventas,pos,opcion,datoacambiar)
                                if x!=1:
                                    a+=1
                                    ventas_menu(matriz_ventas)
                        elif opcion==4:
                            datoacambiar=input("Ingrese el dato por el que desea cambiarlo: ")
                            if validaciones.vfecha(datoacambiar):
                                x=funciones.actualizarventas(matriz_ventas,pos,opcion,datoacambiar)
                                if x!=1:
                                    a+=1
                                    ventas_menu(matriz_ventas)
                        else:
                            print("El número ingresado es incorrecto")
            elif num==4:
                print(matriz_ventas)
                funciones.destruir(matriz_ventas)
                ventas_menu(matriz_ventas)
            else:
                return