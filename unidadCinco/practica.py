""" # Funciones

from unittest import result


def miFuncion():
    print('hola')


for i in range(1, 6):
    print(i)

miFuncion()


def miFuncion(nombre):
    print('Hola, ' + nombre)


miFuncion('Javier')


def suma(a, b):
    print(a + b)


suma(5, 5)

##################################

def matematicas(a, b):
    def suma(a, b):
        print(a + b)

    def resta(a, b):
        print(a - b)

    suma(a, b)
    resta(a, b)
    
matematicas(5, 3)

####################################

def miFuncion(nombre):
    temp = 25
    print('Hola, ' + nombre, 'la temperatura es de ', + temp)
    
miFuncion('Javier')

#Parametros variables

def suma(*args):
    print(args)
    
suma(9*9)

def suma(*args):
    resultado = 0
    
    for arg in args:
        resultado += arg
        
    print(resultado)

suma(2, 2) """

#

def sumador(**kwargs):
    inicial = kwargs['inicial']
    final = kwargs['final']
    
    resultado = 0
    for x in range(inicial, final +1):
        resultado += x

    return resultado

print(sumador(inicial = 15, final = 30))

#anonimas

anonima = lambda: print('hola lambda')
anonima()

anonima = lambda nombre, apellido: print('hola', nombre, apellido)
anonima('juan', 'perez')