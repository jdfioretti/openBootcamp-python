from functools import reduce

# funciones utiles built     #map filter y reduce
# como funciona filter # se pasa por parametro el elemento a filtrar
# si es true mantiene el numero, y si es false lo elimina
# aplica una funcion a todos los elementos de una lista


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def miFuncion(x):
    if x % 2 == 0:
        return True

    return False


resultado = filter(lambda x: x % 2 == 1,  numeros)  # otra opcion
# resultado = filter(miFuncion, numeros)
print(list(resultado))

# map - aplica una funcion a todos los elementos de un iterable
# aplica una funcion a todos los elementos de una lista, indiscriminadamente(a diferencia de filter)


def cuadrado(x):
    return x * x


resultado1 = map(cuadrado, numeros)
print(list(resultado1))

# reduce - antes era parte de python, pero lo eliminaron. Ahora hay que usarlo mediante un
# modulo from functools import reduce
# reduce va a ejecutar la funcion sobre la lista, hasta que esta se quede con un solo elemento


def suma(a, b):             # las fc con reduce necesitan dos parametros
    print(f'a ={a} b={b}')  # vemos lo que sucede internamente
    return a + b

# a es el primer valor, y b el segundo. La suma de estos se guarda en a y vuelve a empezar


res = reduce(suma, numeros)
print(res)

# reduce devuelve un unico resultado a traves de una lista


# zip - agrega iterables en una tupla y los devuelve - conbina listas y tuplas

cursos = ['java', 'python', 'git']
asistentes = [15, 20, 4]
demo = zip(cursos, asistentes)
print(list(demo))

# si en una de las listas hubiera menos valores, solo asocia la cantidad menor de uno.

# all() - devuelve true si todos los elementos de una lista son true (son todos 'and')
# any() - si alguno es true (son todos 'or')

# -------------------------

# round - redondea al valor mas proximo. Si es entre .1 y .4 al anterior, si es .5 a .9 al siguiente

a = 5.5
b = 5.4
c = 5.6

print(round(a))
print(round(b))
print(round(c))

# min - me devuelve cual es el minimo de una lista

print(min(2, 3, 4, 5, 9, 3, 1))

# pow - sirve para elevar

print(pow(2, 3))


# sorted para ordenar listas.

lista = ['z', 'b', 'h', 'c', 'a']
ordenada = sorted(lista)
alReves = sorted(lista, reverse=True)
print(ordenada)
print(alReves)


# input - Sirve para solicitar datos a un usuario

a = input('Como te llamas?: ')
print(f'Hola, {a}')

user = input('Usuario: ')
passwd = input('password: ')

print(f'Usuario: {user} password: {passwd}')


# --------------------------
# como convertir un digito a un string

secreto = 50

valor = 0
while valor != secreto:
    valor = int(input('Ingresa un numero: '))

    if valor > secreto:
        print('Muy alto')
        continue

    if valor < secreto:
        print('Muy bajo')
        continue 
print('Acertaste!')

