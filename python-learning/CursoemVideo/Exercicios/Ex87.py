def matriz_python():
    matriz = list()
    axis0 = list()
    soma_pares = 0
    soma_coluna = 0

    for c1 in range(0, 3):
        for c2 in range(0, 3):
            n = int(input(f'Write a {c2 + 1}° number: '))
            axis0.append(n)
        matriz.append(axis0[:])
        axis0.clear()

    print(f'''
Linha 1: {matriz[0][0]} {matriz[0][1]} {matriz[0][2]}
Linha 2: {matriz[1][0]} {matriz[1][1]} {matriz[1][2]}
Linha 3: {matriz[2][0]} {matriz[2][1]} {matriz[2][2]}
''')
    for p in matriz:
        for i in p:
            if i % 2 == 0:
                soma_pares += i

    col1 = matriz[0][2]
    col2 = matriz[1][2]
    col3 = matriz[2][2]

    soma_coluna = col1 + col2 + col3

    print(f'A soma dos valores pares inseridos é: {soma_pares}')
    print(f'A soma dos valor da terceira coluna é: {soma_coluna}')
    print(f'O maior valor da segunda linha é: {max(matriz[1][:])}')
matriz_python()