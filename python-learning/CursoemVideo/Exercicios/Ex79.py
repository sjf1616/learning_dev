def valores_unicos():
    lista = list()
    for i in range(0, 5):
        num = int(input('Write a number: '))
        if num not in lista:
            lista.append(num)
    print(f'O valores únicos na lista são: {sorted(lista)}')

valores_unicos()