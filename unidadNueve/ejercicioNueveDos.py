from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = filter(lambda num: num % 2 == 1, numeros)

suma = reduce(lambda a, b: a + b, resultado)
print(suma)

