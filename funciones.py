matriz = [
    ["hola", "como", 1],
    ["estas", "hoy", 2]
]

def organizar(matriz):

    #pre: recibe una matriz
    #pos: devuelve la matriz organizada por id descendiente

    x = 0
    for i in range(matriz[0]):
        x += 1

    nombres = [[("dato + %i", lambda y: y + 1) * x] for ("dato + %i", lambda e: e + 1) * x in matriz[0]]
    matriz_r = [[id, nombre[:6], artista[:7], genero[:6]] for id, nombre, artista, genero in matriz]

    for i in range(len(matriz_r)):
        matriz_r[i][2] = matriz_r[i][2].capitalize()
        matriz_r[i][1] = matriz_r[i][1].capitalize()
        matriz_r[i][3] = matriz_r[i][3].capitalize()

    matriz_o = sorted(matriz_r, key=lambda x: (-x[0], x[1]))

    return matriz_o

def crear(stock="no", cliente="no", ventas="no"):

    #pre: pide una de las tres matrices, stock, cliente o ventas
    #pos: devuelve una matriz con una nueva fila creada y orgnaizada

    flag = 0

    while flag == 0:
        if ventas == "no":
            if stock == "no":
                cliente.append([])

                for i in range(len(cliente[0]) - 2):
                    nomb = input(f"Ingrese el {cliente[0][i + 1]}")
                    cliente[len(cliente) - 1].append(nomb)



def leer():
    return
