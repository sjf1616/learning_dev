from random import randint

def maior_menor():
    tupla = tuple(randint(0, 50) for i in range(0, 5))
    print(tupla)
    print(f'O maior valor na tupla é {max(tupla)}')
    print(f'O menor valor na tupla é {min(tupla)}')


maior_menor()


