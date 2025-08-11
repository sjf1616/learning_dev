from random import randint

def adivinhando_numero():
    tentativas = 0
    s = randint(0, 10)
    i = ' '
    while i != s:
        i = int(input('Digite um palpite: '))
        tentativas += 1
        if i == s:
            print(f'\033[32m PARABENS! VOCÊ ACERTOU!\033[m ')
        else:
            print(f'\033[31m VOCÊ ERROU! TENTE NOVAMENTE!\033[m ')
    print(f'O número total de palpites foi \033[35m{tentativas}\033[m')

adivinhando_numero()