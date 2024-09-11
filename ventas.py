from funciones import crear_ventas, leer, actualizarventas, destruir, organizar_ventas
from matriz_stock import matriz_stock
from matriz_cliente import matriz_cliente
from validaciones import vfecha, vcorreo, vnumero, vtexto, 
matriz_ventas=[]
def ventas_menu(matriz_ventas):
    print("Tenga en cuenta lo siguiente:")
    print("1- Crear")
    print("2- Leer")
    print("3- Actualizar")
    print("4- Borrar archivo")

    num=int(input("Ingrese lo que desea hacer: "))
    
    if num==1:
        correo=input("Ingrese el correo del Usuario: ")
        if vcorreo(correo):
            producto=input("Ingrese el nombre del objeto: ")
            producto.capitalize()
            cantidad=input("Ingrese la cantidad vendida: ")
            if vnumero(cantidad):
                fecha=input("Ingrese la fecha con formato DD-MM-AAAA: ")
                if vfecha(fecha):
                    x=crear_ventas(matriz_stock,matriz_cliente,matriz_ventas,producto,correo,fecha)
                    ventas_menu(matriz_ventas)

                    if x==1:
                        print("El correo o el nombre del producto estan mal escritos")
    elif num==2:
        leer(matriz_ventas)
        ventas_menu(matriz_ventas)
    elif num==3:
        a=0
        while a==0:
            leer(matriz_ventas)
            pos=int(input("Ingrese el ID del stock que desea actualizar"))

            print("Tenga en cuenta lo siguiente: ")
            print("1- Nombre del Producto")
            print("2- Cantidad Vendida")
            print("3- Correo del cliente")
            print("4- Fecha")

            opcion=input("Ingrese una opción: ")

            if opcion==1:
                datoacambiar=input("Ingrese el dato por el que desea cambiarlo: ")
                if vtexto(datoacambiar):
                    x=actualizarventas(matriz_ventas,pos,opcion,datoacambiar)
                    if x!=1:
                        a+=1
                        ventas_menu(matriz_ventas)
            elif opcion==2:
                datoacambiar=input("Ingrese el dato por el que desea cambiarlo: ")
                if datoacambiar.isnumeric():
                    x=actualizarventas(matriz_ventas,pos,opcion,datoacambiar)
                    if x!=1:
                        a+=1
                        ventas_menu(matriz_ventas)
            elif opcion==3:
                datoacambiar=input("Ingrese el dato por el que desea cambiarlo: ")
                if vcorreo(datoacambiar):
                    x=actualizarventas(matriz_ventas,pos,opcion,datoacambiar)
                    if x!=1:
                        a+=1
                        ventas_menu(matriz_ventas)
            elif opcion==4:
                datoacambiar=input("Ingrese el dato por el que desea cambiarlo: ")
                if vfecha(datoacambiar):
                    x=actualizarventas(matriz_ventas,pos,opcion,datoacambiar)
                    if x!=1:
                        a+=1
                        ventas_menu(matriz_ventas)
            else:
                print("El número ingresado es incorrecto")
                    
    elif num==4:
        destruir(matriz_ventas)
        ventas_menu(matriz_ventas)
    else:
        return