from funciones import crear_clientes, leer, destruir, actualizarcliente
from validaciones import vidmatriz
def clientes_menu(matriz_clientes):
        flag=0
        while flag==0:
            num = int(input("Seleccione una opcion: 1 crear, 2 leer, 3 actualizar, 4 eliminar, 5 volver al principio: "))
            if num == 1:
                nom = input("Nombre del cliente: ")
                tel = int(input("Teléfono del cliente: "))
                cor= input("Ingrese correo del cliente: ")
                crear_clientes(matriz_clientes, nom, tel, cor)
            elif num == 2:
                leer(matriz_clientes, clientes=1)
            elif num == 3:
                pos=int(input("Ingrese el ID del cliente que desea actualizar: "))
                if vidmatriz(matriz_clientes, pos):
                    print("Tenga en cuenta lo siguiente: ")
                    print("1- Nombre y apellido.")
                    print("2- Teléfono.")
                    print("3- Correo.")

                    opciones=int(input("Ingrese el valor a cambiar: "))
                    if opciones==1:
                        objeto=input("Nombre y Apellido actualizado: ")
                        actualizarcliente(matriz_clientes, pos, opciones, objeto)
                    elif opciones==2:
                        objeto=int(input("Teléfono actualizado del cliente: "))
                        actualizarcliente(matriz_clientes, pos, opciones, objeto)
                    elif opciones==3:
                        objeto=input("Mail actualizado del cliente: ")
                        actualizarcliente(matriz_clientes, pos, opciones, objeto)
                    else:
                        print("El número ingresado es incorrecto.")
                        flag=0
            elif num == 4:
                pos=int(input("Ingrese ID del cliente a eliminar: "))
                destruir(matriz_clientes, pos)
            else:
                flag=1
                return
            