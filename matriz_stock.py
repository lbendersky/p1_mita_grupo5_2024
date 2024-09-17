from funciones import crear_stock, leer, actualizarstock, destruir
import validaciones


def stock_menu(matriz_stock):
    flag = 0
    while flag == 0:
        num = input("seleccione una opcion: 1 crear, 2 leer, 3 actualizar, 4 eliminar, 5 volver al principio: ")

        if validaciones.vnumero(num):

            num=int(num)
            if num == 1:
                
                band=0
                
                while band==0:
                    prod = input("Nombre del producto: ")
                    if validaciones.vtexto(prod)==True:
                        band=1
                        
                band=0   
                while band==0:
                    cant = (input("Cantidad del producto: "))
                    if validaciones.vnumero(cant):
                        cant=int(cant)
                        band=1
                        
                crear_stock(matriz_stock, prod, cant)\
                
            elif num == 2:
                if validaciones.vmatrizvacia(matriz_stock):
                    leer(matriz_stock, stock=1)
            elif num == 3:
                
                if validaciones.vmatrizvacia(matriz_stock):
                
                    band=0
                    while band==0:
                        pos=(input("Ingrese el ID del stock que desea actualizar: "))
                        if validaciones.vnumero(pos):
                            pos=int(pos)
                            if validaciones.vidmatriz(matriz_stock,pos):
                                band=1

                    band=0
                    while band==0:
                        
                        print("Tenga en cuenta lo siguiente: ")
                        print("1- Nombre")
                        print("2- Cantidad")

                        
                        while band==0:
                            opciones=(input("Ingrese el valor a cambiar: "))
                            if validaciones.vnumero(opciones) and opciones=="1" or opciones=="2":
                                opciones=int(opciones)
                                band=1
                            else:
                                print("El numero ingresado es incorrecto")

                        if opciones==1:
                            
                            band=0
                            while band==0:
                                objeto = input("Ingrese nombre del producto: ")
                                if validaciones.vtexto(objeto):
                                    band=1
                                    
                        elif opciones==2:
                            
                            band=0
                            while band==0:
                                objeto = (input("Ingrese cantidad del producto: "))
                                if validaciones.vnumero(objeto):
                                    objeto=int(objeto)
                                    band=1
                        else:
                            print("El número ingresado es incorrecto")

                    actualizarstock(matriz_stock, pos, opciones, objeto)
            elif num == 4:
                
                if validaciones.vmatrizvacia(matriz_stock):
                
                    band=0
                    while band==0:
                        pos = (input("Ingrese el ID del producto que desea eliminar: "))
                        if validaciones.vnumero(pos):
                            pos=int(pos)
                            if validaciones.vidmatriz(matriz_stock,pos):
                                band=1

                    destruir(matriz_stock, pos)
            elif num == 5:
                flag = 1
                return 
            else:
                print("Ingrese un numero correcto")