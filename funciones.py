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
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))

        if nombre.isalpha == True and cantidad.isnumeric() == True:
            stock.append([])

            stock[len(stock) - 1][0] = stock[0][0] + 1
            stock[len(stock) - 1][1] = nombre
            stock[len(stock) - 1][2] = cantidad

            stock_org = organizar_stock(stock)

            return stock_org
        
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




def leer():
    return
