# -*- coding: utf-8 -*-

from copy import copy, deepcopy
import numpy as np

"""
Algoritmo de booth

Suma:
1+1=10-->0 acarreo 1
1+0=1
0+1=1
0+0=0
1+1+1=11-->1 acarreo 1

Ejemplo:
2*3
mult1 = [0,1,0]
mult2 = [0,1,1]

1) Pasar a ca2
mult1 = [0,1,0] --> [1,1,0]
mult2 = [0,1,1] --> [1,0,1]
2) Reemplzar en una matriz:

            Mult1   Mult2
N.Binario[[0 1 0 | 0 0 0 | 0]
N.ca2     [1 1 0 | 0 0 0 | 0]
          [0 0 0 | 0 1 1 | 0]]
                     ^
                     |
                  N.Binario

3) Iteraciones == Número de bits

    00 o 11 --> Desplazar a la Derecha
    01 --> T=T+P --> Desplazar a la Derecha
    10 --> T=T+S --> Desplazar a la Derecha

   Si matriz(2,5)==1 y matriz(2,6)==0 entonces
        sumar terceraFila + segundaFila
        terceraFila = desplazar a la Derecha terceraFila

   Si matriz(2,5)==1 y matriz(2,6)==1 o matriz(2,5)==0 y matriz(2,6)==0 entonces
        terceraFila = desplazar a la Derecha terceraFila

   Si matriz(2,5)==1 y matriz(2,6)==1 o matriz(2,5)==0 y matriz(2,6)==0 entonces
        sumar terceraFila + primeraFila
        terceraFila = desplazar a la Derecha terceraFila

4) Dezplazar
terceraFila = desplazar a la Derecha terceraFila
"""

def sumaBinaria(sumando1, sumando2):
    long = len(sumando1)
    pos = len(sumando1)-1
    acarreo = 0
    res = np.zeros(len(sumando1), dtype='int')

    for i in range(0,long):
        if sumando1[pos]==1 and sumando2[pos]==1 and not acarreo:
            res[pos]=0
            acarreo = 1

        elif sumando1[pos]==1 and sumando2[pos]==1 and acarreo:
            res[pos] = 1
            acarreo = 1

        elif sumando1[pos] == 1 and sumando2[pos] == 0 and not acarreo:
            res[pos] = 1
            acarreo = 0
        elif sumando1[pos] == 1 and sumando2[pos] == 0 and acarreo:
            res[pos] = 0
            acarreo = 1

        elif sumando1[pos] == 0 and sumando2[pos] == 1 and not acarreo:
            res[pos] = 1
            acarreo = 0
        elif sumando1[pos] == 0 and sumando2[pos] == 1 and acarreo:
            res[pos] = 0
            acarreo = 1

        elif sumando1[pos] == 0 and sumando2[pos] == 0 and not acarreo:
            res[pos] = 0
            acarreo = 0

        elif sumando1[pos] == 0 and sumando2[pos] == 0 and acarreo:
            res[pos] = 1
            acarreo = 0

        else:
            print "Error"
            print sumando1[pos]
            print sumando2[pos]
            print acarreo

        pos -= 1
    return res

def complemento(numero):
    leng = len(numero)
    for i in range(leng):
        if numero[i]==0:
            numero[i]= 1
        else:
            numero[i]= 0

    uno = np.zeros(len(numero),dtype='int')
    uno[-1]=1
    numero = sumaBinaria(numero,uno)
    return numero


def algoritmo_boot(mult1, mult2):
    columnas = len(mult1)+len(mult2)+1
    matriz = np.zeros((3,columnas), dtype='int')
    m1 = len(mult1)
    m2 = columnas
    aux = deepcopy(mult1)
    compl = complemento(aux)

    for i in range(m1):
        for j in range(m1):
            if i == 0:
                matriz[i][j]= mult1[j]
            if i == 1:
                matriz[i][j] = compl[j]

    for i in range(m2):
        cont = 0
        for j in range((m2-1)/2,m2-1):
            if i == 2:
                matriz[i][j]= mult2[cont]
                cont = cont+1

    print "Matriz Inicial: \n",matriz

    for i in range(len(mult1)):
        if str(matriz[2][columnas-2])+str(matriz[2][columnas-1])=="10":
            suma = sumaBinaria(matriz[2],matriz[1])
            matriz[2] = suma
            auxj=columnas-1
            for j in range(columnas):
                matriz[2][auxj]=matriz[2][auxj-1]
                auxj -= 1

            print "Iteración: %d" %(i+1)
            print matriz

        elif str(matriz[2][columnas-2])+str(matriz[2][columnas-1])=="11" or str(matriz[2][columnas-2])+str(matriz[2][columnas-1])=="00":
            auxj = columnas - 1
            for j in range(columnas):
                matriz[2][auxj] = matriz[2][auxj - 1]
                auxj -= 1

            print "Iteración: %d" %(i+1)
            print matriz

        elif str(matriz[2][columnas - 2]) + str(matriz[2][columnas - 1]) == "01":
            suma = sumaBinaria(matriz[2], matriz[0])
            matriz[2] = suma
            auxj = columnas - 1
            for j in range(columnas):
                matriz[2][auxj] = matriz[2][auxj - 1]
                auxj -= 1

            print "Iteración: %d" %(i+1)
            print matriz
        else:
            print "Error"


    auxj = columnas - 1
    for j in range(columnas):
        matriz[2][auxj] = matriz[2][auxj - 1]
        auxj = auxj - 1

    print "Ultima Iteración"
    return matriz


mult1 = [0,1,0]
mult2 = [0,1,1]

print algoritmo_boot(mult1,mult2)