def vender(ventas):
    
    band=0
    cont=0
    
    while band==0:
        
        ventas.append([])
    
        band2=0

        while band2==0:
            d=int(input("Dia: "))
            if d>31 or d==0:
                print("Ingrese una fecha adecuada entre 1 y 31")
            else:
                band2=1
                
        band2=0

        while band2==0:
            m=int(input("Mes: "))
            if m>12 or m==0:
                print("Ingrese un mes adecuado entre 1 y 12")
            else:
                band2=1
                
        band2=0

        while band2==0:
            a=int(input("Año: "))
            if a<1000 or a>9999:
                print("Ingrese solo numeros de cuatro digitos")
            else:
                band2=1
        
        
        idcomprador= int(input("Id del comprador: "))
        idobjeto= int(input("Id del objeto a vender: "))
        cantidad= int(input("Cantidad a vender: "))
        valor= int(input("Valor: "))

        ventas[cont].append(f"{d}/{m}/{a}")
        ventas[cont].append(idcomprador)
        ventas[cont].append(idobjeto)
        ventas[cont].append(cantidad)
        ventas[cont].append(valor)
        
        masventa=int(input("Para registrar otra venta, presione 1. Para terminar, presione 2: "))
        
        if masventa==2:
            band=1
        else:
            cont+=1
            
    return ventas
    
print(vender([]))