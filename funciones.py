import validaciones, json
############################################################STOCK############################################################


def organizar_stock(stock_des):

    """pre: recibe matriz de stock desorganizada"""
    """pos: devuelve la matriz organizada por id descendiente"""

    stock_r = [[id, nombre, cantidad] for id, nombre, cantidad in stock_des]

    for i in range(len(stock_r)):
        stock_r[i][1] = stock_r[i][1].capitalize()

    stock_o = sorted(stock_r, key=lambda x: (-x[0], x[2]))

    return stock_o


def crear_stock(stock, nombre, cantidad,idventas=0):

    """pre: recibe matriz de stock, nombre del producto y cantidad del mismo"""
    """pos: devuelve la matriz con una nueva fila creada y organizada y tres columnas: id|nombre|cantidad"""

    if idventas>0:
        stock.append([])
        stock[len(stock) - 1].append(idventas)
    else:
        id = [fila[0] for fila in stock]
        mayor = max(id)
        stock.append([])
        stock[len(stock) - 1].append(mayor+1)
    
    stock[len(stock) - 1].append(nombre)
    stock[len(stock) - 1].append(cantidad)

    stock_org = organizar_stock(stock)

    try:
        with open(r"p1_mita_grupo5_2024\archivos_csv\productos.txt","a",encoding="UTF-8") as archivo_stock:
            archivo_stock.write(f"{len(stock)};{nombre};{cantidad}\n")
    except FileNotFoundError:
        print("El archivo 'productos.txt' no fue encontrado")
    except OSError:
        print("Ha sucedido un error con el archivo 'producto.txt'")
    finally:  
        return stock_org

def actualizarstock(stock, pos, opciones, objeto):
    """pre: Ingresa la matriz de stock, la posición (ID), la opción elegida (Que se quiere actualizar) y el dato que se cambiará."""
    """Pos: Se devuelven los datos cambiados en las posiciones y lugares solicitados."""
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
        
        try:
            with open(r"p1_mita_grupo5_2024\archivos_csv\productos.txt","r",encoding="UTF-8") as archivo:
                lineas=archivo.readlines()
        except FileNotFoundError:
            print("El archivo 'productos.txt' no fue encontrado")
            return
        except OSError:
            print("Ha sucedido un error con el archivo 'productos.txt'")
            return
        
        id,nombre,cantidad=lineas[pos-1].split(";")
        
        if opciones==1:
            stock[x][1]=objeto
            lineas[pos-1] = (f"{id};{objeto};{cantidad}")
            
        elif opciones==2:
            
            #stock[x][2]=objeto
            #lineas[pos-1] = (f"{id};{nombre};{objeto}\n")
            
            if objeto==0:
                stock=destruir(stock,pos,2)
                print()
                print("El producto fue eliminado ya que su cantidad es 0")
                return stock
            else:
                stock[x][2]=objeto
                lineas[pos-1] = (f"{id};{nombre};{objeto}\n")

        try: 
            with open(r"p1_mita_grupo5_2024\archivos_csv\productos.txt", "w",encoding="UTF-8") as archivo:
                archivo.writelines(lineas)
        except FileNotFoundError:
            print("El archivo 'productos.txt' no fue encontrado")
            return
        except OSError:
            print("Ha sucedido un error con el archivo 'productos.txt'")
            return 
        
        return stock
        
        
            
    
    
        
        
###########################################################CLIENTES###########################################################

        
def organizar_clientes(clientes_des):

    """pre: recibe matriz de clientes desorganizada"""
    """pos: devuelve la matriz organizada por id descendiente"""

    clientes_r = [[id, nombre[:9], telefono, correo] for id, nombre, telefono, correo in clientes_des]

    clientes_o = sorted(clientes_r, key=lambda x: (-x[0], x[2]))

    return clientes_o


def crear_clientes(clientes, nombre, telefono, correo):

    """pre: recibe matriz de clientes, nombre de la persona, telefono y correo"""
    """pos: devuelve la matriz con una nueva fila creada y organizada con cuatro columnas: id|nombre|telefono|correo"""
    clientes.append([])
    clientes[len(clientes) - 1].append(len(clientes))
    clientes[len(clientes) - 1].append(nombre)
    clientes[len(clientes) - 1].append(telefono)
    clientes[len(clientes) - 1].append(correo)

    clientes_org = organizar_clientes(clientes)

    try:
        with open(r"p1_mita_grupo5_2024\archivos_csv\clientes.txt","a",encoding="UTF-8") as archivo_cliente:
            archivo_cliente.write(f"{len(clientes)};{nombre};{telefono};{correo}\n")
    except FileNotFoundError:
        print("El archivo 'clientes.txt' no fue encontrado")
    except OSError:
        print("Ha sucedido un error con el archivo 'clientes.txt'")
    else:
        return clientes_org    

def actualizarcliente(matriz_clientes,pos,opciones,objeto):
    """pre: recibe la matriz cliente, el id del cliente, opcion del parametro a cambiar y objeto es por lo que lo va a cambiar"""
    """pos: devuelve la matriz con el valor especificado cambiado"""

    band=0
    x=-1
    while band==0 and x<len(matriz_clientes)-1:
        x+=1
        if matriz_clientes[x][0]==pos:
            band=1
    if band==0:
        print("No se encontró el ID")
    else:
        
        try:
            
            with open(r"p1_mita_grupo5_2024\archivos_csv\clientes.txt","r",encoding="UTF-8") as archivo:
                lineas=archivo.readlines()
                
            id,nombre,telefono,correo=lineas[pos-1].split(";")
            
            if opciones==1:
                matriz_clientes[x][1]=objeto
                lineas[pos-1] = (f"{id};{objeto};{telefono};{correo}")
            elif opciones==2:
                matriz_clientes[x][2]=objeto
                lineas[pos-1] = (f"{id};{nombre};{objeto};{correo}")
            elif opciones==3:
                matriz_clientes[x][3]=objeto
                lineas[pos-1] = (f"{id};{nombre};{telefono};{objeto}\n")
                
            with open(r"p1_mita_grupo5_2024\archivos_csv\clientes.txt", "w",encoding="UTF-8") as archivo:
                archivo.writelines(lineas)
            
            return matriz_clientes
        
        except FileNotFoundError:
            print("El archivo 'clientes.txt' no fue encontrado")
        except OSError:
            print("Ha sucedido un error con el archivo 'clientes.txt'")



##########################################################VENTAS##########################################################


def organizar_ventas(ventas_des):

    """pre: recibe matriz de ventas desorganizada"""
    """pos: devuelve la matriz organizada por id descendiente"""

    ventas_o = sorted(ventas_des, key=lambda x: (-x["Id"], x["Cantidad"], x["Id_prod"]))

    return ventas_o


def crear_ventas(stock, clientes, ventas, nombre, correo, cantidad, fecha):

    """pre: recibe matriz de ventas, nombre del producto, correo del cliente, cantidad del producto y fecha de la venta"""
    """pos: devuelve la matriz con una nueva fila creada y organizada con seis columnas: id|id del item|id del cliente|nombre del mismo|cantidad vendida|fecha """


    """Encontrar el id con el nombre del producto"""
    prod_stock = [[id, name, cant] for id, name, cant in stock if name == nombre]

    if prod_stock[0][2] < cantidad or len(prod_stock) == 0:
        return 2
    else:
        stock = actualizarstock(stock, prod_stock[0][0], 2, prod_stock[0][2] - cantidad)

    """Encontrar el id y nombre con la casilla de correo"""
    cliente = [[id, name, tele, mail] for id, name, tele, mail in clientes if mail == correo]

    if len(cliente) == 0:
        return 1
    
    encabezados = ("Id", "Id_prod", "Id_clien", "Nombre producto", "Nombre cliente", "Cantidad", "Fecha")
    elementos = [len(ventas) + 1, prod_stock[0][0], cliente[0][0], prod_stock[0][1], cliente[0][1], cantidad, fecha]
    ventas.append(dict(zip(encabezados, elementos)))

    ventas_org = organizar_ventas(ventas)

    try:
        with open(r"p1_mita_grupo5_2024\archivos_csv\ventas.json","w",encoding="UTF-8") as json_ventas:
            json.dump(ventas_org, json_ventas,indent=4)
    except FileNotFoundError:
        print("El archivo 'ventas.json' no fue encontrado")
    except OSError:
        print("Ha sucedido un error con el archivo 'ventas.json'")
    finally:
        return ventas_org, stock


def actualizarventas(matriz_ventas,pos,opcion,datoacambiar,stock):

    """pre: Ingresa la matriz de ventas, la posición (ID), la opción elegida (Que se quiere actualizar) y el dato que se cambiará."""
    """Pos: Se devuelven los datos cambiados en las posiciones y lugares solicitados."""

    for x in range(len(matriz_ventas)):
        if matriz_ventas[x]['Id'] == pos:
            if opcion==1:
                matriz_ventas[x]['Nombre producto']=datoacambiar

                try:
                    with open(r"p1_mita_grupo5_2024\archivos_csv\ventas.json","w",encoding="UTF-8") as json_ventas:
                        json.dump(matriz_ventas, json_ventas)
                except OSError:
                    print("Ha sucedido un error inesperado.")
                finally:
                    return matriz_ventas, stock
                
            if opcion==2:
                matriz_ventas[x]['Nombre cliente']=datoacambiar

                try:
                    with open(r"p1_mita_grupo5_2024\archivos_csv\ventas.json","w",encoding="UTF-8") as json_ventas:
                        json.dump(matriz_ventas, json_ventas)
                except FileNotFoundError:
                    print("El archivo 'ventas.json' no fue encontrado")
                except OSError:
                    print("Ha sucedido un error con el archivo 'ventas.json'")
                finally:
                    return matriz_ventas, stock
                
            if opcion==3:
                if matriz_ventas[x]['Cantidad'] > datoacambiar:
                    stock = actualizarstock(stock, matriz_ventas[x]['Id_prod'], 2, stock[matriz_ventas[x]['Id_prod'] - 1][2] - (matriz_ventas[x]['Cantidad'] - datoacambiar))
                elif matriz_ventas[x]['Cantidad'] < datoacambiar:
                    stock = actualizarstock(stock, matriz_ventas[x]['Id_prod'], 2, stock[matriz_ventas[x]['Id_prod'] - 1][2] - (datoacambiar - matriz_ventas[x]['Cantidad']))

                matriz_ventas[x]['Cantidad']=datoacambiar

                try:
                    with open(r"p1_mita_grupo5_2024\archivos_csv\ventas.json","w",encoding="UTF-8") as json_ventas:
                        json.dump(matriz_ventas, json_ventas)
                except FileNotFoundError:
                    print("El archivo 'ventas.json' no fue encontrado")
                except OSError:
                    print("Ha sucedido un error con el archivo 'ventas.json'")
                finally:
                    return matriz_ventas, stock
                
            if opcion==4:
                matriz_ventas[x]['Fecha']=datoacambiar

                try:
                    with open(r"p1_mita_grupo5_2024\archivos_csv\ventas.json","w",encoding="UTF-8") as json_ventas:
                        json.dump(matriz_ventas, json_ventas)
                except FileNotFoundError:
                    print("El archivo 'ventas.json' no fue encontrado")
                except OSError:
                    print("Ha sucedido un error con el archivo 'ventas.json'")
                finally:
                    return matriz_ventas, stock


def destruir_ventas(dic_ventas, pos, stock):
    
    a=0
    cantventas= dic_ventas[len(dic_ventas) - pos]['Cantidad']
    idventas= dic_ventas[len(dic_ventas) - pos]['Id_prod'] 
    nombreventas= dic_ventas[len(dic_ventas) - pos]['Nombre producto']
    
    for x in range(len(stock)):
        if stock[x][0] == idventas:
            stock[x][2] += cantventas
            a=1
    
    if a==0:
        stock=crear_stock(stock,nombreventas,cantventas,idventas)  
    else:
        actualizarstock(stock,stock[x][0],2,stock[x][2])
    
    dic_ventas.pop(len(dic_ventas) - pos)
    
    try:
        with open(r"p1_mita_grupo5_2024\archivos_csv\ventas.json","w",encoding="UTF-8") as json_ventas:
            json.dump(dic_ventas, json_ventas,indent=4)  
    except FileNotFoundError:
        print("El archivo 'ventas.json' no fue encontrado")
    except OSError:
        print("Ha sucedido un error con el archivo 'ventas.json'")
    finally:
        
        return dic_ventas, stock
        

#################################################################LEER#################################################################

def leer(matriz,f=0, stock=0, clientes=0, ventas=0,):

    if stock == 1:
        if f>=len(matriz):
            return
        else:
           
            fila = matriz[f]
            id, nombre, cantidad = fila
            print(f"| {id :<4}| {nombre :<24}| {cantidad}")
            leer(matriz, f + 1, stock=1) 
                
    elif clientes == 1:
        print(f"| {'Id' :<5}| {'Nombre' :<20}| {'Telefono' :<20}| {'Correo'}")
        print("-" * 75)
        for id, nombre, telefono, correo in matriz:
            print(f"| {id :<5}| {nombre :<20}| {telefono :<20}| {correo}")

    elif ventas == 1:
        for encabezados in matriz[0].keys():
            print(f"|{encabezados :^15}", end=" ")

        print("")
        print("-" * 117)

        for i in range(len(matriz)):
            for elementos in matriz[i].values():
                print(f"|{elementos :^15}", end=" ")
            print("")
    else:
        print("Formato no valido")
        return 
    return 
        

#####################################################Destruir############################################################################


def destruir(a, pos,opcion):
    """pre: Entra la matriz deseada y el ID a buscar"""
    """pos: Se devuelve la matriz con el ID deseado borrado si se encuentra"""
           
    for x in range(len(a)):
        if a[x][0] == pos:
            a.pop(x)
            break
            
    if opcion==1:
        
        try:
            open(r"p1_mita_grupo5_2024\archivos_csv\clientes.txt", "w",encoding="UTF-8")
        except FileNotFoundError:
            print("El archivo 'clientes.txt' no existe")
        except OSError:
            print("Ha sucedido un error con el archivo 'clientes.txt'")
        else:
            file.writelines(f"{ayd};{nomb};{tele};{corr}\n" for ayd, nomb, tele, corr in a)
        file.close()
        return a
    
    elif opcion==2:
        
        try:
            file = open(r"p1_mita_grupo5_2024\archivos_csv\productos.txt", "w",encoding="UTF-8")
        except FileNotFoundError:
            print("El archivo 'productos.txt' no existe")
        except OSError:
            print("Ha sucedido un error con el archivo 'productos.txt'")
        else: 
            file.writelines(f"{ayd};{nomb};{canti}\n" for ayd, nomb, canti in a)
        file.close()
        return a

        
    return False