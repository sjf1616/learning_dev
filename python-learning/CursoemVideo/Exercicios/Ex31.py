d = int(input(f'Qual a distancia?: '))

if d <= 200:
    p_p = d * 0.5
    print(f'O valor da passagem é: R$ {p_p}')
else:
    p_p = d * 0.45
    print(f'O valor da passagem é: R$ {p_p}')