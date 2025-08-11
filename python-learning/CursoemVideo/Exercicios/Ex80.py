def list_repeat():
    lista = list()
    for i in range(0 , 5):
        numero = int(input('Write a value: '))
        if len(lista) == 0:
            lista.append(numero)
        for n in lista:
            if numero > max(lista):
                lista.append(numero)
            elif numero < min(lista):
                lista.insert(0, numero)
    print(f'A lista ordenada é: {lista}')
list_repeat()