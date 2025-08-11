from random import randint

n = int(input('Digite um número: '))

escolhido = randint(1, 5)

print(f'Você acertou' if escolhido == n else f'Você errou, o número escolhido foi {escolhido}')