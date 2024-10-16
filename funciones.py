import validaciones
############################################################STOCK############################################################


def organizar_stock(stock_des):

    #pre: recibe matriz de stock desorganizada
    #pos: devuelve la matriz organizada por id descendiente

    stock_r = [[id, nombre, cantidad] for id, nombre, cantidad in stock_des]

    for i in range(len(stock_r)):
        stock_r[i][1] = stock_r[i][1].capitalize()

    stock_o = sorted(stock_r, key=lambda x: (-x[0], x[2]))

    return stock_o


def crear_stock(stock, nombre, cantidad):

    #pre: recibe matriz de stock, nombre del producto y cantidad del mismo
    #pos: devuelve la matriz con una nueva fila creada y organizada y tres columnas: id|nombre|cantidad

    stock.append([])

    stock[len(stock) - 1].append(len(stock))
    stock[len(stock) - 1].append(nombre)
    stock[len(stock) - 1].append(cantidad)

    stock_org = organizar_stock(stock)

    return stock_org


def actualizarstock(stock, pos, opciones, objeto):
    #pre: Ingresa la matriz de stock, la posición (ID), la opción elegida (Que se quiere actualizar) y el dato que se cambiará.
    #Pos: Se devuelven los datos cambiados en las posiciones y lugares solicitados.
    band=0
    x=-1
    while band==0 and x<len(stock)-1:
        x+=1
        if stock[x][0]==pos:
            band=1

    if band==0:
        print("No se encontró el ID")
        return
    else:
        if opciones==1:
            stock[x][1]=objeto
            return stock
        elif opciones==2:
            stock[x][2]=objeto
            return stock
        
        
###########################################################CLIENTES###########################################################

        
def organizar_clientes(clientes_des):

    #pre: recibe matriz de clientes desorganizada
    #pos: devuelve la matriz organizada por id descendiente

    clientes_r = [[id, nombre[:9], telefono, correo] for id, nombre, telefono, correo in clientes_des]

    clientes_o = sorted(clientes_r, key=lambda x: (-x[0], x[2]))

    return clientes_o


def crear_clientes(clientes, nombre, telefono, correo):

    #pre: recibe matriz de clientes, nombre de la persona, telefono y correo
    #pos: devuelve la matriz con una nueva fila creada y organizada con cuatro columnas: id|nombre|telefono|correo

    clientes.append([])

    clientes[len(clientes) - 1].append(len(clientes))
    clientes[len(clientes) - 1].append(nombre)
    clientes[len(clientes) - 1].append(telefono)
    clientes[len(clientes) - 1].append(correo)

    clientes_org = organizar_clientes(clientes)

    return clientes_org
        

def actualizarcliente(matriz_clientes,pos,opciones,objeto):
    #pre: recibe la matriz cliente, el id del cliente, opcion del parametro a cambiar y objeto es por lo que lo va a cambiar
    #pos: devuelve la matriz con el valor especificado cambiado

    band=0
    x=-1
    while band==0 and x<len(matriz_clientes)-1:
        x+=1
        if matriz_clientes[x][0]==pos:
            band=1
    if band==0:
        print("No se encontró el ID")
    else:
        if opciones==1:
            matriz_clientes[x][1]=objeto
            return matriz_clientes
        elif opciones==2:
            matriz_clientes[x][2]=objeto
            return matriz_clientes
        elif opciones==3:
            matriz_clientes[x][3]=objeto
            return matriz_clientes
        else:
            print("El número ingresado es incorrecto")
            return 


##########################################################VENTAS##########################################################


def organizar_ventas(ventas_des):

    #pre: recibe matriz de ventas desorganizada
    #pos: devuelve la matriz organizada por id descendiente

    ventas_o = sorted(ventas_des, key=lambda x: (-x["Id"], x["Cantidad"], x["Id_prod"]))

    return ventas_o


def crear_ventas(stock, clientes, ventas, nombre, correo, cantidad, fecha):

    #pre: recibe matriz de ventas, nombre del producto, correo del cliente, cantidad del producto y fecha de la venta
    #pos: devuelve la matriz con una nueva fila creada y organizada con seis columnas: id|id del item|id del cliente|nombre del mismo|cantidad vendida|fecha 

    
    #Encontrar el id con el nombre del producto
    prod_stock = [[id, name, cant] for id, name, cant in stock if name == nombre]

    if prod_stock[0][2] < cantidad or len(prod_stock) == 0:
        return 2
    else:
        stock[(len(stock) - 1) - (prod_stock[0][0] - 1)][2] = prod_stock[0][2] - cantidad

    #Encontrar el id y nombre con la casilla de correo
    cliente = [[id, name, tele, mail] for id, name, tele, mail in clientes if mail == correo]

    if len(cliente) == 0:
        return 1
    
    encabezados = ["Id", "Id_prod", "Id_clien", "Nombre producto", "Nombre cliente", "Cantidad", "Fecha"]
    elementos = [len(ventas) + 1, prod_stock[0][0], cliente[0][0], prod_stock[0][1], cliente[0][1], cantidad, fecha]
    ventas.append(dict(zip(encabezados, elementos)))

    ventas_org = organizar_ventas(ventas)



    return ventas_org, stock


def actualizarventas(matriz_ventas,pos,opcion,datoacambiar,stock):

    #pre: Ingresa la matriz de ventas, la posición (ID), la opción elegida (Que se quiere actualizar) y el dato que se cambiará.
    #Pos: Se devuelven los datos cambiados en las posiciones y lugares solicitados.

    for x in range(len(matriz_ventas)):
        if matriz_ventas[x]['Id'] == pos:
            if opcion==1:
                matriz_ventas[x]['Nombre producto']=datoacambiar
                return matriz_ventas, stock
            if opcion==2:
                matriz_ventas[x]['Nombre cliente']=datoacambiar
                return matriz_ventas, stock
            if opcion==3:
                if matriz_ventas[x]['Cantidad'] > datoacambiar:
                    stock[matriz_ventas[x]['Id_prod'] - 1][2] += matriz_ventas[x]['Cantidad'] - datoacambiar
                elif matriz_ventas[x]['Cantidad'] < datoacambiar:
                    stock[matriz_ventas[x]['Id_prod'] - 1][2] -= datoacambiar - matriz_ventas[x]['Cantidad']

                matriz_ventas[x]['Cantidad']=datoacambiar

                return matriz_ventas, stock
            if opcion==4:
                matriz_ventas[x]['Fecha']=datoacambiar
                return matriz_ventas, stock


def destruir_ventas(dic_ventas, pos, stock):
    stock[dic_ventas[len(dic_ventas) - pos]['Id_prod'] - 1][2] += dic_ventas[len(dic_ventas) - pos]['Cantidad']
    dic_ventas.pop(len(dic_ventas) - pos)
    return dic_ventas
        

#################################################################LEER#################################################################


def leer(matriz, stock=0, clientes=0, ventas=0):

    #pre: Ingresa la matriz y a cual pertenece (ej, stock=1)
    #pos: Regresa 1 si mostro el resultado y 0 si no hay ningun parametro en uno

    if stock == 1:
        matriz = organizar_stock(matriz)
        
        print(f"{'Id' :<5}{'Nombre' :<30}{'Cantidad'}")

        print("-" * 45)

        for id, nombre, cantidad in matriz:
            print(f"{id :<5}{nombre :<30}{cantidad}")
    elif clientes == 1:
        print(f"{'Id' :<5}{'Nombre' :<20}{'Telefono' :<20}{'Correo'}")

        print("-" * 60)

        for id, nombre, telefono, correo in matriz:
            print(f"{id :<5}{nombre :<20}{telefono :<20}{correo}")
    elif ventas == 1:
        for encabezados in matriz[0].keys():
            print(f"{encabezados :^10}", end=" ")

        print("")
        print("-" * 85)

        for i in range(len(matriz)):
            for elementos in matriz[i].values():
                print(f"{elementos :^12}", end=" ")
            print("")
    else:
        print("Formato no valido")
        return 
    return 
        

#####################################################Destruir############################################################################


def destruir(a, pos):
    # pre: Entra la matriz deseada y el ID a buscar
    # pos: Se devuelve la matriz con el ID deseado borrado si se encuentra.
    for x in range(len(a)):
        if a[x][0] == pos:
            a.pop(x)
            return a
    return False