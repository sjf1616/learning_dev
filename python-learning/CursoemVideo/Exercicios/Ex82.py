def dividindo_listas():
    listas = []
    pares = []
    impar = []
    while True:
        print('Write Three number')
        for i in range(0, 3):
            number = int(input(f'Write a {i+1}° number: '))
            listas.append(number)
            if number % 2 == 0:
                pares.append(number)
            elif number % 1 == 0:
                impar.append(number)
        c = str(input('Want to continue? [Y/N]: '))
        while c not in 'YyNn':
            c = str(input('Want to continue? [Y/N]: '))
        if c in 'Nn':
            break

    print(f'Os números gerados foram: {listas}')
    print(f'Os números pares gerados foram: {pares}')
    print(f'Os números impar gerados foram: {impar}')

dividindo_listas()