############################################################STOCK############################################################


def organizar_stock(stock_des):

    #pre: recibe matriz de stock desorganizada
    #pos: devuelve la matriz organizada por id descendiente

    stock_r = [[id, nombre[:6], cantidad] for id, nombre, cantidad in stock_des]

    for i in range(len(stock_r)):
        stock_r[i][1] = stock_r[i][1].capitalize()

    stock_o = sorted(stock_r, key=lambda x: (-x[0], x[2]))

    return stock_o


def crear_stock(stock):

    #pre: recibe matriz de stock
    #pos: devuelve la matriz con una nueva fila creada y organizada

    flag = 0

    while flag == 0:
        desicion = int(input("Ingrese 1 si desea continuar, 2 si desea frenar el proceso"))
        if desicion == 1:
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))

            if nombre.isalpha == True and cantidad.isnumeric() == True:
                stock.append([])

                stock[len(stock) - 1][0] = stock[0][0] + 1
                stock[len(stock) - 1][1] = nombre
                stock[len(stock) - 1][2] = cantidad

                stock_org = organizar_stock(stock)

                flag = 1
                return stock_org
        else:
            return
        

###########################################################CLIENTES###########################################################

        
def organizar_clientes(clientes_des):

    #pre: recibe matriz de clientes desorganizada
    #pos: devuelve la matriz organizada por id descendiente

    clientes_r = [[id, nombre[:6], telefono, correo] for id, nombre, telefono, correo in clientes_des]

    for i in range(len(clientes_r)):
        clientes_r[i][1] = clientes_r[i][1].capitalize()

    clientes_o = sorted(clientes_r, key=lambda x: (-x[0], x[2]))

    return clientes_o


def crear_clientes(clientes):

    #pre: recibe matriz de clientes
    #pos: devuelve la matriz con una nueva fila creada y organizada

    flag = 0

    while flag == 0:
        nombre = input("Ingrese el nombre de la persona: ")
        cantidad = int(input("Ingrese numero telefonico del cliente:"))
        correo = str(input("Ingrese correo electronico del cliente: "))

        if nombre.isalpha == True and cantidad.isnumeric() == True and correo.isalpha() == True:
            clientes.append([])

            clientes[len(clientes) - 1][0] = clientes[0][0] + 1
            clientes[len(clientes) - 1][1] = nombre
            clientes[len(clientes) - 1][2] = cantidad
            clientes[len(clientes) - 1][3] = correo

            clientes_org = organizar_clientes(clientes)

            return clientes_org
        

##########################################################VENTAS##########################################################


def organizar_ventas(ventas_des):

    #pre: recibe matriz de ventas desorganizada
    #pos: devuelve la matriz organizada por id descendiente

    ventas_r = [[id, id_it, id_per, nombre[:6], cantidad, fecha] for id, id_it, id_per, nombre, cantidad, fecha in ventas_des]

    for i in range(len(ventas_r)):
        ventas_r[i][1] = ventas_r[i][2].capitalize()

    ventas_o = sorted(ventas_r, key=lambda x: (-x[4], x[3], x[2]))

    return ventas_o


def crear_ventas(stock, clientes, ventas):

    #pre: recibe matriz de ventas
    #pos: devuelve la matriz con una nueva fila creada y organizada

    flag = 0

    while flag == 0:
        nombre = int(input("Ingrese el nombre del producto vendido: "))
        correo = str(input("Ingrese casilla de correo del cliente"))
        cantidad = int(input("Ingrese la cantidad del producto vendido: "))
        fecha = int(input("Ingrese fecha en la que se realizo la venta: "))


        if nombre.isalpha == True and cantidad.isnumeric() == True and correo.isalpha() == True and fecha.isnumeric() == True:
            ventas.append([])

            #Buscar id mas grande al no organizarlo por id
            grande = 0
            for i in range(len(ventas)):
                if ventas[i][0] > grande:
                    grande = ventas[i][0]

            ventas[len(ventas) - 1][0] = grande + 1

            #Encontrar el id con el nombre del producto
            x = 0
            for name in stock[x][1]:
                x += 1
                if name == nombre.capitalize():
                    ventas[len(ventas) - 1][1] = stock[x][0]

            #Encontrar el id y nombre con la casilla de correo
            x = 0
            for mail in clientes[x][3]:
                x += 1
                if mail == correo:
                    ventas[len(ventas) - 1][2] = clientes[x][0]
                    ventas[len(ventas) - 1][3] = clientes[x][1]

            ventas[len(ventas) - 1][4] = cantidad
            ventas[len(ventas) - 1][5] = fecha

            ventas_org = organizar_ventas(ventas)

            return ventas_org


#################################################################LEER#################################################################


def leer(matriz, stock=0, clientes=0, ventas=0):

    #pre: Ingresa la matriz y a cual pertenece (ej, stock=1)
    #pos: Regresa 1 si mostro el resultado y 0 si no hay ningun parametro en uno

    if stock == 1:
        print(f"{'Id' :>4}{'Nombre' :^10}{'Cantidad' :<4}")

        print("-" * 20)

        for id, nombre, cantidad in matriz:
            print(f"{id :>4}{nombre :^10}{cantidad :<4}")
    elif clientes == 1:
        print(f"{'Id' :>4}{'Nombre' :^10}{'Telefono' :^10}{'Correo' :<4}")

        print("-" * 30)

        for id, nombre, telefono, correo in matriz:
            print(f"{id :>4}{nombre :^10}{telefono :^10}{correo :<4}")
    elif ventas == 1:
        print(f"{'Id de la venta' :>4}{'Id del producto' :^10}{'Id de la persona' :^10}{'Nombre de la persona' :^10}{'Cantidad' :^10}{'Fecha' :<4}")

        print("-" * 70)

        for id_ven, id_prod, id_per, nombre, cantidad, fecha in matriz:
            print(f"{id_ven :>4}{id_prod :^10}{id_per :^10}{nombre :^10}{cantidad :^10}{fecha :<4}")
    else:
        print("Formato no valido")
        return 0
    
    return 1
############################################################################################################################

def actualizarcliente(cliente):
    print("Tenga en cuenta lo siguiente:")
    print("1- ID")
    print("2- Datos del Cliente")
    n=int(input("Ingrese el dato a actualizar: "))
    if n==1:
        flag=0
        band=0
        x=-1
        while band==0 and x<len(cliente)-1:
            x+=1
            if cliente[x][0]==n:
                band=1
            while flag==0:
                if band==1:
                    cliente[x][0]=int(input("Ingrese el ID del cliente por el que desea cambiarlo"))
                    return cliente
                else:
                    print("No se encontró el ID")
                    print("Reingrese el ID a buscar")
                    flag==1
    elif n==2:
        flag=0
        pos=int(input("Ingrese el ID del cliente que desea actualizar"))
        band=0
        x=-1
        while band==0 and x<len(cliente)-1:
            x+=1
        while flag==0:
            if cliente[x][0]==pos:
                band=1
        if band==0:
            print("No se encontró el ID")
        else:
            print("Tenga en cuenta lo siguiente: ")
            print("1- Nombre y Apellido")
            print("2- Mail")
            print("3- Telefono")
            opciones=int(input("Ingrese el valor a cambiar: "))

            if opciones==1:
                cliente[x][1]=int(input("Ingrese el Nombre y Apellido actualizado: "))
                return cliente
            elif opciones==2:
                cliente[x][2]=int(input("Ingrese el mail actualizado del cliente: "))
                return cliente
            elif opciones==3:
                cliente[x][3]=int(input("Ingrese el telefono actualizado del cliente"))
                return cliente
            else:
                print("El número ingresado es incorrecto")
                flag==0
        
def actualizarstock(stock):
    print("Tenga en cuenta lo siguiente:")
    print("1- ID")
    print("2- Datos del Objeto")
    n=int(input("Ingrese el dato a actualizar: "))
    if n==1:
        flag=0
        band=0
        x=-1
        while band==0 and x<len(stock)-1:
            x+=1
            if stock[x][0]==n:
                band=1
            while flag==0:
                if band==1:
                    stock[x][0]=int(input("Ingrese el ID del stock por el que desea cambiarlo"))
                    return stock
                else:
                    print("No se encontró el ID")
                    print("Reingrese el ID a buscar")
                    flag==1
    elif n==2:
        flag=0
        pos=int(input("Ingrese el ID del stock que desea actualizar"))
        band=0
        x=-1
        while band==0 and x<len(stock)-1:
            x+=1
        while flag==0:
            if stock[x][0]==pos:
                band=1
        if band==0:
            print("No se encontró el ID")
    else:
        print("Tenga en cuenta lo siguiente: ")
        print("1- Nombre")
        print("2- Cantidad")
        print("3- Precio de Compra")
        print("4- Precio de Venta")
        opciones=int(input("Ingrese el valor a cambiar: "))

        if opciones==1:
            stock[x][1]=int(input("Ingrese el nombre de el objeto: "))
            return stock
        elif opciones==2:
            stock[x][2]=int(input("Ingrese la cantidad de Objetos que dispone actualmente: "))
            return stock
        elif opciones==3:
            stock[x][3]=int(input("Ingrese el Precio de Compra del Objeto"))
            return stock
        elif opciones==4:
            stock[x][4]=int(input("Ingrese el Precio de Venta del Objeto"))
        else:
            print("El número ingresado es incorrecto")
            flag==0

def actualizarventas(ventas):
    print("Tenga en cuenta lo siguiente:")
    print("1- ID de Comprador")
    print("2- ID de Objeto")
    print("3- Información de la Venta")
    n=int(input("Ingrese el dato a actualizar: "))
    if n==1:
        flag=0
        band=0
        x=-1
        while band==0 and x<len(ventas)-1:
            x+=1
            if ventas[x][0]==n:
                band=1
            while flag==0:
                if band==1:
                    ventas[x][0]=int(input("Ingrese el ID de venta por el que desea cambiarlo"))
                    return ventas
                else:
                    print("No se encontró el ID")
                    print("Reingrese el ID a buscar")
                    flag==1
    elif n==2:
        flag=0
        band=0
        x=-1
        while band==0 and x<len(ventas)-1:
            x+=1
            if ventas[x][0]==n:
                band=1
            while flag==0:
                if band==1:
                    ventas[x][0]=int(input("Ingrese el ID de venta por el que desea cambiarlo"))
                    return ventas
                else:
                    print("No se encontró el ID")
                    print("Reingrese el ID a buscar")
                    flag==1
    else:
        flag=0
        pos=int(input("Ingrese el ID de la venta que desea actualizar"))
        band=0
        x=-1
        while band==0 and x<len(ventas)-1:
            x+=1
        while flag==0:
            if ventas[x][0]==pos:
                band=1
        if band==0:
            print("No se encontró el ID")
        else:
            print("Tenga en cuenta lo siguiente: ")
            print("1- Cantidad")
            print("2- Valor")
            print("3- Fecha")
            opciones=int(input("Ingrese el valor a cambiar: "))

            if opciones==1:
                ventas[x][1]=int(input("Ingrese el Nombre y Apellido actualizado: "))
                return ventas
            elif opciones==2:
                ventas[x][2]=int(input("Ingrese el mail actualizado del stock: "))
                return ventas
            elif opciones==3:
                x1=int(input("Ingrese el día a cambiar: "))
                x2= int(input("Ingrese el mes a cambiar: "))
                x3= int(input("Ingrese el año a cambiar: "))
                return ventas
            else:
                print("El número ingresado es incorrecto")
                flag==0

def destruir(a):
    band=0
    x=-1

    while band==0 and x<len(a)-1:
        pos = int(input("Ingrese el ID de cliente que desea eliminar: "))

        x+=1
        if a[x][0]==pos and pos.isnumeric()==True:
            a.pop(x)
            return a
        else: 
            print("No se encontró el ID del cliente")