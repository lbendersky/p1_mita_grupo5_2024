from funciones import crear_clientes, leer, destruir, actualizarcliente

def clientes_menu(matriz_clientes):
    num = int(input("seleccione una opcion: 1 crear, 2 leer, 3 actualizar, 4 eliminar, 5 volver al principio: "))

    if num == 1:
        nom = input("Nombre del cliente: ")
        tel = int(input("Teléfono del cliente: "))
        cor= input("Ingrese correo del cliente: ")
        crear_clientes(matriz_clientes, nom, tel, cor)
        clientes_menu()
    elif num == 2:
        leer(matriz_clientes, stock=1)
        clientes_menu()
    elif num == 3:
        pos=int(input("Ingrese el ID del cliente que desea actualizar"))

        print("Tenga en cuenta lo siguiente: ")
        print("1- Nombre")
        print("2- Teléfono")
        print("3- Correo")

        opciones=int(input("Ingrese el valor a cambiar: "))
        #Verificacion: si se ingresa 4 tiene que pedirme ingresar otro valor (arreglar)
        if opciones==1:
            matriz_clientes[pos][1]=int(input("Ingrese el Nombre y Apellido actualizado: "))
            return matriz_clientes
        elif opciones==2:
            matriz_clientes[pos][2]=int(input("Ingrese el mail actualizado del cliente: "))
            return matriz_clientes
        elif opciones==3:
            matriz_clientes[pos][3]=int(input("Ingrese el telefono actualizado del cliente"))
            return matriz_clientes
        else:
            print("El número ingresado es incorrecto")
            flag==0
    
        actualizarcliente(matriz_clientes, pos, opciones, objeto)
        clientes_menu()
    elif num == 4:
        destruir(matriz_clientes)
        clientes_menu()
    else:
        return
