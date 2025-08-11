from random import randint

def palpites_mega():
    j = int(input('Quantos jogos deseja gerar: '))
    palpites = list()
    jogos = list()
    for i in range(0, j):
        while len(palpites) != 6:
            numero = randint(1, 60)
            if numero not in palpites:
                palpites.append(numero)
        jogos.append(palpites[:])
        palpites.clear()
    print(f'O total de jogos foram: {j}')
    print(f'Esses foram os números escolhidos')
    for e, i in enumerate(jogos):
        print(f'Jogo {e+1}: {sorted(i)}')

palpites_mega()