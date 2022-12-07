# Numeros primos


def numPrimos(numero):
    if numero < 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if (numero % i) == 0:
                return False
            return True


def num():
    numero = int(input('Ingrese un número: '))
    resultado = numPrimos(numero)

    if resultado is True:
        print('El número es primo')
    else:
        print('El número no es primo')


if __name__ == '__main__':
    num()
