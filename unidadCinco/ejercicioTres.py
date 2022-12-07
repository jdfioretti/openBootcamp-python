# Año Bisiesto

year = int(input('Ingrese el año: \n'))


def bisiesto(year):
    if year % 100 == 0 and year % 400 == 0:
        print('Es bisiesto')
    elif year % 4 == 0 and year % 100 != 0:
        print('Es bisiesto')
    else:
        print('No es año bisiesto')


print(bisiesto(year))
