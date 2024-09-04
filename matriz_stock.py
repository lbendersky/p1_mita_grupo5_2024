from random import randint
def mostrar_matriz(a):
    for filas in range(len(a)):
        for colum in range(len(a[0])):
            print(f"{a[filas][colum] : ^17}", end=" ")
        print()

stock=["Id","Verdura/Fruta","Cantidad","precio de compra","precio de venta"]
identificacion=[1,2,3,4,5,6,7,8,9,10]
matriz_stock=[]
#crear y llenar la matriz en 0
for fil in range(len(identificacion)+1):
    matriz_stock.append([])
    for col in range (len(stock)):
        matriz_stock[fil].append(0)
#llenar cada columna con valores de (1-10) de manera ascendiente:
flag = -1
for i in range (len(matriz_stock)):
    for f in range(len(matriz_stock[0])):
        if i ==0:
            matriz_stock[i][f]= stock[f]
        else:
            matriz_stock[i][f]= identificacion[flag]
    flag += 1
#llenar la matriz con valores de 0, excluyendo la fila 'id':
for j in range (1, len(matriz_stock)):
    for i in range (1,len(matriz_stock[0])):
        matriz_stock[j][i] = 0


