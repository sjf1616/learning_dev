import random as rd

def resultado():
    print(f'Jogador escolheu {jogador}')
    print(f'O computador escolheu {comp}')


def par_impar():
    trofeu = 0
    global comp
    global jogador

    while True:
        comp = rd.randint(0, 10)
        par_ou_impar = str(input('Escolha "Par" ou "Impar":  ')).lower().strip()
        jogador = int(input('Jogue o seu número: '))
        if par_ou_impar[0] in 'p':
            if (jogador + comp) % 2 == 0:
                resultado()
                print(f'O jogador venceu!')
                trofeu += 1
            elif (jogador + comp) % 2 == 1:
                resultado()
                print(f'O computador venceu')
                break
        elif par_ou_impar[0] in 'i':
            if (jogador + comp) % 2 == 1:
                resultado()
                print(f'O jogador venceu!')
                trofeu += 1
            elif (jogador + comp) % 2 == 0:
                resultado()
                print(f'O computador venceu')
                break
    print(f'O total de vitórias consecutivas foi de {trofeu}')

par_impar()