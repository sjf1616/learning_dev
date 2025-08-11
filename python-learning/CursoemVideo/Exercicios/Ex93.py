def cadastro_jogador():
    jogador = dict()
    jogos = dict()
    total_jogos = int(input('Qual foi o total e jogos: '))
    tot_gols = 0
    for i in range(0, total_jogos):
        gol = int(input(f'Quantos gols ele fez no {i+1}° jogo: '))
        tot_gols += gol
        jogos[f'Partida {i+1}'] = gol
    jogador['Nome'] = str(input('Nome: '))
    jogador['Partidas'] = total_jogos
    jogador['Jogos'] = jogos
    jogador['Total gols'] = tot_gols
    print('-=' * 15)
    print(f'{'JOGADOR':^30}')
    print('-=' * 15)
    for k, v in jogador.items():
        if k not in 'Jogos':
            print(f'{k} = {v}')
        elif k in 'Jogos':
            print('-=' * 15)
            print(f'{'GOLS POR PARTIDA':^30}')
            print('-=' * 15)
            for k, v in jogos.items():
                print(f'{k}° = {v}')
cadastro_jogador()