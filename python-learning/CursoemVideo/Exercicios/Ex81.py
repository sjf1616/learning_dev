def extr_dados():
    lista = list()
    total_number = 0
    while True:
        print('Write a Three numbers')
        for i in range(0, 3):
            lista.append(int(input(f'Write {i+1}° number: ')))
            total_number += 1
        continuar = str(input('Deseja continuar? [S/N]: '))
        while continuar not in 'NnSs':
            continuar = str(input('Deseja continuar? [S/N]: '))
        if continuar in 'Nn':
            break
    if 5 in lista:
        print(f'O valor 5 foi digitado')
    else:
        print(f'O valor 5 não foi digitado')
    print(f'A lista em ordem decrescente é {sorted(lista, reverse=True)}')
    print(f'O total de números digitados foi: {total_number}')

extr_dados()