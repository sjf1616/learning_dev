def pares_impares():
    lista_unica = list()
    pares = list()
    impar = list()
    for i in range(0, 7):
        n = int(input(f'Write a {i+1}° number: '))
        if n % 2 == 0:
            pares.append(n)
        else:
            impar.append(n)
    lista_unica.append(pares[:])
    sorted(pares)
    lista_unica.append(impar[:])
    sorted(impar)
    pares.clear()
    impar.clear()
    print(f'O valores adicionados em ordem crescente foram: {lista_unica}')
pares_impares()