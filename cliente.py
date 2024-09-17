from funciones import crear_clientes, leer, destruir, actualizarcliente
import validaciones

def clientes_menu(matriz_clientes):
        flag=0
        while flag==0:
            num = (input("Seleccione una opcion: 1 crear, 2 leer, 3 actualizar, 4 eliminar, 5 volver al principio: "))
            
            if validaciones.vnumero(num):
                
                num=int(num)
                
                if num == 1:
                    
                    band=0
                    while band==0:
                        nom = input("Nombre y apellido del cliente: ")
                        if validaciones.vnombre(nom):
                            nom=validaciones.vnombre(nom)
                            band=1
                        
                    band=0    
                    while band==0:
                        tel = (input("Teléfono del cliente (549(Codigo de area)XXXXXXXX): "))
                        if validaciones.vtelefono(tel):
                            band=1
                       
                    band=0
                    while band==0:     
                        cor= input("Ingrese correo del cliente (nombre@correo.com): ")
                        if validaciones.vcorreo(cor):
                            band=1
                
                    crear_clientes(matriz_clientes, nom, tel, cor)
                    
                elif num == 2:
                    if validaciones.vmatrizvacia(matriz_clientes):
                        leer(matriz_clientes, clientes=1)
                        
                elif num == 3:
                    
                    if validaciones.vmatrizvacia(matriz_clientes):
                        band=0
                        while band==0:
                            pos=(input("Ingrese el ID del cliente que desea actualizar: "))
                            if validaciones.vnumero(pos):
                                pos=int(pos)
                                if validaciones.vidmatriz(matriz_clientes, pos):
                                    band=1
                        
                        band=0
                        while band==0: 
                                    
                            print("Tenga en cuenta lo siguiente: ")
                            print("1- Nombre y apellido.")
                            print("2- Teléfono.")
                            print("3- Correo.")

                            while band==0:
                                opciones=input("Ingrese el valor a cambiar: ")
                                if validaciones.vnumero(opciones) and opciones in ("1","2","3"):
                                    opciones=int(opciones)
                                    band=1
                                else:
                                    print("El numero ingresado es incorrecto")
                            
                            if opciones==1:
                                
                                band=0
                                while band==0:
                                    objeto=input("Nombre y Apellido actualizado: ")
                                    if validaciones.vnombre(objeto):
                                        objeto=validaciones.vnombre(objeto)
                                        band=1
                                        
                            elif opciones==2:
                                
                                band=0
                                while band==0:
                                    objeto=(input("Teléfono actualizado del cliente: "))
                                    if validaciones.vtelefono(objeto):
                                        band=1
                                
                            elif opciones==3:
                                
                                band=0
                                while band==0:
                                    objeto=input("Mail actualizado del cliente: ")
                                    if validaciones.vcorreo(objeto):
                                        band=1

                            else:
                                print("El número ingresado es incorrecto.")
                                
                        actualizarcliente(matriz_clientes, pos, opciones, objeto)
                    
                elif num == 4:
                    
                    if validaciones.vmatrizvacia(matriz_clientes):
                        
                        band=0
                        while band==0:
                            pos=(input("Ingrese ID del cliente a eliminar: "))
                            if validaciones.vnumero(pos):
                                pos=int(pos)
                                if validaciones.vidmatriz(matriz_clientes,pos):
                                    band=1
                        
                        destruir(matriz_clientes, pos)
                        
                elif num == 5:
                    flag=1
                    return
                else:
                    print("Ingrese un numero correcto")
            