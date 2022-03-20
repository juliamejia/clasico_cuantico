#programa simulacion de lo clasico a lo cuantico
# Julia Mejia


import math
import LIBRERIA


#1. los experimentos de las canicas con coeficientes booleanos

def experimento_canica(matriz,vector,cantidad):
    click = 0
    if len(matriz) == len(vector):
        guardar = vector
        while click != cantidad:
            guardar = LIBRERIA.accionMatVector(matriz,guardar)
            click = click + 1
        return guardar
        print (guardar)
    else:
        print('Longitudes inexactas para hacer la accion')
        return None
    
# funcion que halla  la potencia de una matriz 
def potencia (a,b):
    matriz = a
    for i in range (1,b):
        res = LIBRERIA.productoMatriz(matriz,a)
        matriz=res
    return matriz

#2. experimentos de las multiples rendijas clasico probabilistico, con mas de dos rendijas
# el usuario ingresa las probabilidades de que las balas se muevan de cada rendija
#a cada objetivo, y luego la matriz se multplica por si misma
def experimentos_rendijas(matriz, vector, disparo):
    res1=potencia(matriz,disparo)
    res2=LIBRERIA.accionMatVector(res1,vector)
    return(res2)


#4Cree una función para graficar con un diagrama de barras que muestre las probabilidades de un vector de estados.

def probabilidad (vector):
    x=[]
    y=[]
    for i in range (len(vector)):
        m=vector[i]
        y=y+[LIBRERIA.moduloComp(m[0],m[1])*100]
    for i in range (len(vector)):
        x=x+[i]

def main():
    #ingresa una matriz booleana , el estado inicial y el numero de clicks 
    matriz1 = [[(0,0),(0,0),(0,0),(0,0),(1,0),(0,0)],
             [(0,0),(0,0),(0,0),(1,0),(0,0),(0,0)],
             [(0,0),(1,0),(0,0),(0,0),(0,0),(1,0)],
             [(0,0),(0,0),(0,0),(1,0),(0,0),(0,0)],
             [(0,0),(0,0),(1,0),(0,0),(0,0),(1,0)],
             [(1,0),(0,0),(0,0),(0,0),(1,0),(0,0)]]
    estado1 = [(23,0),(3,0),(12,0),(1,0),(4,0),(2,0)]
    click1 = 3
    print("-----------------------EXPERIMENTO_CANICA-----------------------------------------")
    print(experimento_canica(matriz1,estado1,click1))

    print()
    print("-----------------------POTENCIA-----------------------------------------")
    print()

    matriz2= [[(0,0),(0,0),(1/9,0),(1/27,0),(5/4,0),(10/3,0)],
             [(0,0),(0,0),(1/9,0),(5/9,0),(5/9,0),(5/18,0)],
             [(1/9,0),(2/9,0),(1/6,0),(1/3,0),(1/18,0),(1/9,0)],
             [(2/9,0),(1/9,0),(1/3,0),(1/6,0),(1/9,0),(1/18,0)],
             [(2/9,0),(4/9,0),(1/9,0),(3/5,0),(0,0),(0,0)],[(4/9,0),(2/9,0),(2/9,0),(1/9,0),(0,0),(0,0)]]
    click2= 1
    print(potencia(matriz2,click2))

    print()
    
    print("-----------------------EXPERIMENTOS -----------------------------------------")
    print()
          
    matriz3=[[(0,0),(0,0),(1/18,0),(1/9,0),(5/18,0),(5/9,0)],
           [(0,0),(0,0),(1/9,0),(1/18,0),(5/9,0),(5/18,0)],
           [(1/9,0),(2/9,0),(1/6,0),(1/3,0),(1/18,0),(1/9,0)],
           [(2/9,0),(1/9,0),(1/3,0),(1/6,0),(1/9,0),(1/18,0)],
           [(2/9,0),(4/9,0),(1/9,0),(2/9,0),(0,0),(0,0)],
           [(4/9,0),(2/9,0),(2/9,0),(1/9,0),(0,0),(0,0)]]
    estado3=[(4/5,0),(1/5,0),(0,0),(0,0),(0,0),(0,0)]
    click3 = 1
    print (experimentos_rendijas(matriz3,estado3,click3))

main()

    
