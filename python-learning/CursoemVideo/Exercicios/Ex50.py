def sum_pares():
    s = 0
    for i in range(0, 6):
        n = int(input(f'Digite o {i+1}ª número: '))
        if n % 2 == 0:
            s += n
    print(f'A soma total dos números pares foi: \033[32m{s}')

sum_pares()