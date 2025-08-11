def tabela_precos():
    tabela = ('Chocolate', 1.99,
              'Maionese', 8.90,
              'Frango', 7.89,
              'Café', 4.57)

    for item in range(0, len(tabela), 2):
        print(f'{tabela[item]:.<30}', end='')
        print(f'R$ {tabela[item + 1]}')

tabela_precos()