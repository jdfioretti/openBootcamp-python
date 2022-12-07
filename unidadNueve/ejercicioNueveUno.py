from functools import reduce

paises = list(set(input('Ingrese paises separados por coma: ').split(',')))
paises.sort()
paises = reduce(lambda p1, p2: p1+', '+p2, paises)
print(f'Listado de Paises :{paises}')
