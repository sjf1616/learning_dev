selecao = list()
jogador = dict()
jogos = list()

def cores():
    return {
        'clean':'\033[m',
        'green':'\033[32m',
        'red':'\033[31m'
    }

def designer(x):
    cor = cores()
    print('=-' * 15)
    print(f'{cor['green']}{x:^30}{cor['clean']}')
    print('=-' * 15)


def main():
    designer('Cadastro Seleção')
    cadastro_jogador()
    mostrar_jogador()

def cadastro_jogador():
    total_jogos = int(input('Quantos jogos foram jogados: '))
    while True:
        jogador['name'] = str(input('Nome do jogador: ')).lower().strip().capitalize()
        for i in range(0, total_jogos):
            score = int(input(f'Gol na {i+1}° partida: '))
            jogos.append(score)
        jogador['jogos'] = jogos
        selecao.append(jogador.copy())
        if break_loop():
            break

def break_loop():
    cor = cores()
    q = str(input('Deseja continuar? [S/N]: '))[0].lower().strip()
    while q not in 'sn':
        q = str(input(f'{cor['red']}Resposta errada! Tente novamente... (Apenas S(Sim) ou N(Não): '))[0].lower().strip()
    if q in 'n':
        return True


def mostrar_jogador():
    while True:
        mostrar = str(input('Qual jogador quer buscar: ')).lower().strip().capitalize()
        buscar = [a for a in selecao if a['name'] == mostrar]
        for i in buscar:
            print(f'\nJogador buscado: {i['name']}')
            for e, a in enumerate(i['jogos']):
                print(f'Jogo {e+1} = {a} gol(s)')
        if break_loop():
            break
main()