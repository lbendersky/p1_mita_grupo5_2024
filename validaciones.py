import re
from datetime import datetime

#Texto (vtexto)
#Nombre y apellido (vnombre) (Capitalizarlo)
#Numero (vnumero)
#Correo (vcorreo)
#Fecha (vfecha)
#Telefono (vtelefono)
#Si el id que ingreso esta en cada matriz:
    #vidclientes matriz_clientes
    #vidstock matriz_stock
    #vidventas matriz_ventas
#Seleccion de matriz (vsmatriz)

def vtexto(texto):
    
    patron= r'[A-Za-z]'
    
    if re.match(patron,texto):
        return True
    else:
        print("Solo se permite ingresar texto")   
        return False
        
def vnombre(nombre):

    if vtexto(nombre)==False:
        return 
    else:
        palabras=nombre.split()
        if len(palabras)==2:
            return " ".join(palabras.strip().title() for palabras in palabras) #Capitaliza el texto en formato title
        else:
            print("Ingrese nombre y apellido de forma adecuada")
            return 
        
def vnumero(numero):
    
    patron= r'\d+'
    
    if re.match(patron,numero):
        return numero.replace(" ", "")
    else:
        print("Solo se permite ingresar numeros")   
        return 
    
def vcorreo(correo):
    
    #"Ingresar correo (formato nombre@correo.com): "
    patron= r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    if re.match(patron,correo):
        return correo
    else:
        print("Ingrese el correo en el formato adecuado")   
        return 
     
def vfecha(fecha):
    
    # (DD/MM/AAAA)
    patron = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
    
    if not re.match(patron, fecha):
        print("El formato de la fecha no es válido.")
        return
    
    dia, mes, año = map(int, fecha.split("/"))

    fecha_valida = True
    if mes in [4, 6, 9, 11] and dia > 30: 
        fecha_valida = False
    elif dia > 31: 
        fecha_valida = False
    
    if not fecha_valida:
        print("La fecha no es válida.")
        return

    fecha_usuario = datetime(año, mes, dia)

    fecha_actual = datetime.now()

    if fecha_usuario > fecha_actual:
        print("La fecha introducida es futura.")
    else:
        return fecha_usuario.strftime('%d/%m/%Y')    
    
    
def vtelefono(telefono):
    
    #Formato: (549(Numero de hasta 3 digitos)xxxxxxxx)
    patron= r"^549\d{1,3}\d{8}$"
    
    if re.match(patron,telefono):
        return telefono
    else:
        print("Ingrese el numero de telefono en el formato adecuado")   
        return 
    
#def vidclientes(idclientes):
    
    
"""while True:
    
    if vtelefono(input("telefono: ")):
        print("Correcto")
        break"""


#vtexto(input("Input: "))   
#print(vcorreo(input("Ingresar correo (formato nombre@correo.com): ")))