def soma_numeros():
    s = 0
    for i in range(1, 500):
        if i % 3 == 0:
            s += i
            print(f'\033[32m{i}\033[m')
    print(f'A soma dos números é: \033[31m{s}')


soma_numeros()