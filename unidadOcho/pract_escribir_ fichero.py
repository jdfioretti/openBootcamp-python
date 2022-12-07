# como se escribe un fichero

f = open('miFichero.txt', 'a')
f.write('Hola Mundo\n')
f.write('Hola que tal\n')
f.close()

f = open('miFichero.txt', 'w')

lista = [

    'una linea\n',
    'dos lineas\n',
    'tres lineas'
]

f.writelines(lista)
f.close()

############################


def escribe(fichero, datos):
    f = open(fichero, 'w')

    for linea in datos:
        if not linea.endswith('\n'):
            linea = linea + '\n '
        f.write(linea)

    f.close()


lista = [

    'una linea',
    'dos lineas',
    'tres lineas'


]

escribe('miFicehro.txt', lista)
