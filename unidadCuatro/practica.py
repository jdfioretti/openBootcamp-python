lista = [1,2,3,4,5]
tupla = {1,2,3,'a', 'b'}

for valorActual in tupla:
    print(valorActual)


for numero in range(1, 7):
    print(numero) 

lista = ['Hola', 'Mensaje', 'Adios']

for palabra in lista:
    print('Palabra actual: ', palabra)

    if palabra == 'Mensaje':
        print("He encontrado la palabra mensaje")
        break 

lista = [3,2,1,5,4]
print(lista)

listaOrdenada = sorted(lista)
print(listaOrdenada)

listaOrdenada = sorted(lista, reverse=True)
print(listaOrdenada)

#**********************************************************

from nis import match
from unittest import case



""" valor = 5

match valor:
    case 1:
    print("el valor es 1")
    case 2:
    print("el valor es 2")
    case 3:
    print("el valor es 3") """



# Ver el tema del "else" en el for.
