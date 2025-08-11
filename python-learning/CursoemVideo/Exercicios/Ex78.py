def maior_menor():
    valores = []
    for i in range(0, 5):
        valores.append((int(input('Digite os valores: '))))
    print(f'O maior valor da lista é {max(valores)} na posição {valores.index(max((valores)))}')
    print(f'O menor valor da lista é {min(valores)} na posição {valores.index(min(valores))}')

maior_menor()