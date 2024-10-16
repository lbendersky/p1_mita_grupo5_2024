from funciones import crear_stock, leer, actualizarstock, destruir
import validaciones


def stock_menu(matriz_stock):
    flag = 0
    while flag == 0:
        print()
        num=input("Tenga en cuenta lo siguiente:\n1- Crear \n2- Leer \n3- Actualizar \n4- Borrar archivo \n5- Volver al menu \n\nIngrese lo que desea hacer: ")
        print()
        if validaciones.vnumero(num):

            num=int(num)
            if num == 1:
                
                prod = input("Nombre del producto: ").capitalize()
                        
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
                        
                        print("Tenga en cuenta lo siguiente: \n1- Nombre \n2- Cantidad")
                        
                        while band==0:
                            opciones=(input("Ingrese el valor a cambiar: "))
                            if validaciones.vnumero(opciones) and opciones in ("1","2"):
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

                    try:
                        file = open(r"proyecto\p1_mita_grupo5_2024\archivos_csv\productos.txt", "w")
                    except:
                        print("No se pudo abrir el archivo")
                    else: 
                        file.writelines(f"{ayd};{nomb};{canti}\n" for ayd, nomb, canti in matriz_stock)
                        file.close()

            elif num == 5:
                flag = 1
                return 
            else:
                print("\nIngrese un numero correcto\n")