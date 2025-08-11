from random import  randint

numeros = list()

def sorteia():
    for _ in range(0, 5):
        s = randint(0, 100)
        numeros.append(s)
    print(numeros)

def somaPar(lista):
    pares = [x for x in lista if x % 2 == 0]
    for _ in pares:
        print(f'+ {_}', end=' ')
    print(f'= {sum(pares)}')

sorteia()
somaPar(numeros)