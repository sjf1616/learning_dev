def list_analise():
    galera = list()
    pessoa = list()
    pesadas = list()
    leves = list()
    total_peoples = 0
    while True:
        print(f'Write a Three peoples')
        for i in range(0, 3):
            pessoa.append(str(input('Write a name of person: ')))
            pessoa.append(float(input('Write a weight of person: ')))
            galera.append(pessoa[:])
            pessoa.clear()
            total_peoples += 1
        for p in galera:
            if p[1] >= 90:
                pesadas.append(p[:])
                p.clear()
            else:
                leves.append(p[:])
                p.clear()
                
        c = str(input('Want to continue [Y/N]: '))
        while c not in 'YyNn':
            c = str(input('\033[31mThis answer is wrong, please write only Y to yes or N to no\033[m'))
        if c in 'Nn':
            break

    print(f'Total of peoples is {total_peoples}')
    print(f'As pessoas mais pesadas são: {pesadas}')
    print(f'As pessoas mais leves são: {leves}')
list_analise()