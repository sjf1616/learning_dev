import random

def bot():
    e = random.randint(1, 3)
    if e == 1:
        return 'pedra'
    elif e == 2:
        return 'papel'
    elif e == 3:
        return  'tesoura'

def jokenpo():
    i = str(input('Pedra, Papel ou Tesoura: ')).strip().lower()

    x = bot()
    print(f'O bot escolheu a opção {x}')
    if i == x:
        print(f'Empate')
    elif (x == 'pedra' and i == 'papel') or (x == 'papel' and i == 'tesoura') or (x == 'tesoura' and i == 'pedra'):
        print(f'Jogador venceu')
    else:
        print(f'Bot venceu')

jokenpo()