import math


def verifica_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return  True

numero = int(input('Digite um número: '))

if verifica_primo(numero):
    print(f'O número {numero} é primo')
else:
    print(f'O número {numero} não é primo')