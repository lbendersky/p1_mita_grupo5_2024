from funciones import crear_clientes, leer, destruir, actualizarcliente

def clientes_menu(matriz_clientes):
        flag=0
        while flag==0:
            num = int(input("Seleccione una opcion: 1 crear, 2 leer, 3 actualizar, 4 eliminar, 5 volver al principio: "))

            if num == 1:
                nom = input("Nombre del cliente: ")
                tel = int(input("Teléfono del cliente: "))
                cor= input("Ingrese correo del cliente: ")
                crear_clientes(matriz_clientes, nom, tel, cor)
                clientes_menu(matriz_clientes)
            elif num == 2:
                leer(matriz_clientes, clientes=1)
                clientes_menu(matriz_clientes)
            elif num == 3:
                pos=int(input("Ingrese el ID del cliente que desea actualizar: "))

                print("Tenga en cuenta lo siguiente: ")
                print("1- Nombre y apellido.")
                print("2- Teléfono.")
                print("3- Correo.")

                opciones=int(input("Ingrese el valor a cambiar: "))
                #Verificacion: si se ingresa 4 tiene que pedirme ingresar otro valor (arreglar)
                if opciones==1:
                    objeto=input("Nombre y Apellido actualizado: ")
                    actualizarcliente(matriz_clientes, pos, opciones, objeto)
                    return matriz_clientes
                elif opciones==2:
                    objeto=int(input("Teléfono actualizado del cliente: "))
                    actualizarcliente(matriz_clientes, pos, opciones, objeto)
                    return matriz_clientes
                elif opciones==3:
                    objeto=input("Mail actualizado del cliente: ")
                    actualizarcliente(matriz_clientes, pos, opciones, objeto)
                    return matriz_clientes
                else:
                    print("El número ingresado es incorrecto.")
                    flag=0
            
                actualizarcliente(matriz_clientes, pos, opciones, objeto)
                clientes_menu(matriz_clientes)
            elif num == 4:
                destruir(matriz_clientes)
                clientes_menu(matriz_clientes)
            else:
                return
