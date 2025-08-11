def matriz_python():
    matriz = list()
    axis0 = list()
    axis1 = list()
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


matriz_python()