import re
from datetime import datetime

#Funciones de validacion:
#Texto (vtexto)
#Nombre y apellido (vnombre) (Capitalizarlo)
#Numero (vnumero)
#Correo (vcorreo)
#Fecha (vfecha)
#Telefono (vtelefono)
#Si el id que ingreso esta en cada matriz (vidmatriz)

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
            return " ".join(palabras.strip().title()[:6] for palabras in palabras) #Capitaliza el texto en formato title
        else:
            print("Ingrese nombre y apellido de forma adecuada")
            return 


def vnumero(numero):
    
    """ if str(numero).isdigit():
        return True
    else:
        print("Solo se permite ingresar números.")
        return False """
    #Implemento try y except
    try:
        int(numero)
    except ValueError:
        print("Solo se permite ingresar números.")
        return False
    else:
        return True
    
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
    if mes in [2, 4, 6, 9, 11] and dia > 30: 
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
        print("Ingrese el numero de telefono en el formato adecuado.")   
        return 


def vidmatriz(matriz, id):
    for fila in matriz:
        if fila[0]==id:
            return True  
    print("El id no se encuentra en la matriz.")
    return False


def viddic(dic, id):
    for i in range(len(dic)):
        if dic[i]['Id'] == id:
            return True
    print("El id no se encuentra en la matriz.")
    return False


def vmatrizvacia(matriz):
    
    if not matriz:
        print("La matriz está vacía")
        return False

    for fila in matriz:
        if fila:  
            return True
    print("La matriz está vacía")
    return False


def login(contra, lugar_del_puesto):
    posibles_usuarios = [
        {"usuario": "Jefe", "contraseña": "jefazo", "stock": 1, "clientes": 1, "ventas": 1},
        {"usuario": "Stock", "contraseña": "stock", "stock": 1, "clientes": 0, "ventas": 0},
        {"usuario": "Cliente", "contraseña": "cliente", "stock": 0, "clientes": 1, "ventas": 0},
        {"usuario": "Ventas", "contraseña": "ventas", "stock": 0, "clientes": 0, "ventas": 1}
        ]
    
    if contra == posibles_usuarios[lugar_del_puesto - 1]["contraseña"]:
        usuario = posibles_usuarios[lugar_del_puesto - 1]

    return usuario