def tabela_campeonato_brasileiro():
    tabela = ('Botafogo',
              'Palmeiras',
              'Flamengo',
              'Fortaleza',
              'Internacional',
              'São Paulo',
              'Corinthians',
              'Bahia',
              'Cruzeiro',
              'Vasco da gama',
              'Vitória',
              'Atlético',
              'Fluminense',
              'Grêmio',
              'Juventude',
              'Bragantino',
              'Athlético-PR',
              'Criciúma',
              'Atlético Goianiense',
              'Cuiabá')

    print(f'Os cincos primeiros times são: {tabela[:5]}')
    print(f'O últimos 4 colocados são: {tabela[-4:]}')
    print(f'Em ordem alfabética ficaria {sorted(tabela)}')
    print(f'A posição da chapecoense é: {tabela.count('Chapecoense')}')

tabela_campeonato_brasileiro()