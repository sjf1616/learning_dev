def analise_dados():
    tupla = tuple(input('Write a number: ') for i in range(0, 4))
    print(f'O número 9 apareceu {tupla.count('9')} vezes')
    print(f'A posição do valor 3 é {tupla.index('3')}')
    print(f'Os números pares foram: ', end='')
    for n in tupla:
        inteiro = int(n)
        if inteiro % 2 == 0:
            print(f'{n}', end=' -> ')
        print(f'fim')
analise_dados()