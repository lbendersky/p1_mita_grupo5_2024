from funciones import crear_clientes, leer, destruir, actualizarcliente
import validaciones

def clientes_menu(matriz_clientes):
        flag=0
        while flag==0:
            num=input("Tenga en cuenta lo siguiente:\n1- Crear \n2- Leer \n3- Actualizar \n4- Borrar archivo \n5- Volver al menu \n\nIngrese lo que desea hacer: ")
            
            if validaciones.vnumero(num):
                
                num=int(num)
                
                if num == 1:
                    
                    band=0
                    while band==0:
                        nom = input("Nombre y apellido del cliente o 0 para salir: ")
                        if nom=="0":
                            flag=1
                        elif validaciones.vnombre(nom):
                            nom=validaciones.vnombre(nom)
                            band=1
                        
                    band=0    
                    while band==0:
                        tel = (input("Teléfono del cliente (549(Codigo de area)XXXXXXXX) ó ingrese 0 para salir: "))
                        if tel=="0":
                            flag=1
                        elif validaciones.vtelefono(tel):
                            band=1
                       
                    band=0
                    while band==0:     
                        cor= input("Ingrese correo del cliente (nombre@correo.com) ó ingrese 0 para salir: ").lower()
                        if cor=="0":
                            flag=1
                        elif validaciones.vcorreo(cor):
                            band=1
                
                    crear_clientes(matriz_clientes, nom, tel, cor)
                    
                elif num == 2:
                    if validaciones.vmatrizvacia(matriz_clientes):
                        leer(matriz_clientes, clientes=1)
                        
                elif num == 3:
                    
                    if validaciones.vmatrizvacia(matriz_clientes):
                        band=0
                        while band==0:
                            pos=(input("Ingrese el ID del cliente que desea actualizar o ingrese 0 para salir: "))
                            if pos=="0":
                                flag=1
                            elif validaciones.vnumero(pos):
                                pos=int(pos)
                                if validaciones.vidmatriz(matriz_clientes, pos):
                                    band=1
                        
                        band=0
                        while band==0: 
                                    
                            print("Tenga en cuenta lo siguiente: \n1- Nombre y apellido \n2- Telefono \n3- Correo\n0- Para salir")

                            while band==0:
                                opciones=input("Ingrese el valor a cambiar: ")
                                if opciones=="0":
                                    flag=1
                                elif validaciones.vnumero(opciones) and opciones in ("1","2","3"):
                                    opciones=int(opciones)
                                    band=1
                                else:
                                    print("El numero ingresado es incorrecto")
                            
                            if opciones==1:
                                
                                band=0
                                while band==0:
                                    objeto=input("Nombre y Apellido actualizado ó ingrese 0 para salir: ")
                                    if objeto=="0":
                                        flag=1
                                    elif validaciones.vnombre(objeto):
                                        objeto=validaciones.vnombre(objeto)
                                        band=1
                                        
                            elif opciones==2:
                                
                                band=0
                                while band==0:
                                    objeto=(input("Teléfono actualizado del cliente ó ingrese 0 para salir: "))
                                    if objeto=="0":
                                        flag=1
                                    elif validaciones.vtelefono(objeto):
                                        band=1
                                
                            elif opciones==3:
                                
                                band=0
                                while band==0:
                                    objeto=input("Mail actualizado del cliente ó ingrese 0 para salir: ")
                                    if objeto=="0":
                                        flag=1
                                    elif validaciones.vcorreo(objeto):
                                        band=1

                            else:
                                print("El número ingresado es incorrecto.")
                                
                        actualizarcliente(matriz_clientes, pos, opciones, objeto)
                    
                elif num == 4:
                    
                    if validaciones.vmatrizvacia(matriz_clientes):
                        
                        band=0
                        while band==0:
                            pos=(input("Ingrese ID del cliente a eliminar ó ingrese 0 para salir: "))
                            if pos=="0":
                                flag=1
                            elif validaciones.vnumero(pos):
                                pos=int(pos)
                                if validaciones.vidmatriz(matriz_clientes,pos):
                                    band=1
                        
                        destruir(matriz_clientes, pos)
                        
                elif num == 5:
                    flag=1
                    return
                else:
                    print("\nIngrese un numero correcto\n")