# -*- coding: utf-8 -*-

def ord_insercion(lista):
    for indice in range(1, len(lista)):
        valor = lista[indice]
        i = indice - 1
        while i>=0:
            if valor < lista[i]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                i -=1
            else:
                break


lista = [7,6,4,5,8,2,3,9,4]

ord_insercion(lista)

print lista

