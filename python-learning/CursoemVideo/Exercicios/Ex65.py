def maior_menor():
    cores = {
        'clean':'\033[m',
        'green':'\033[32m',
        'red':'\033[31m'
    }
    count = 0
    maior = 0
    menor = 0
    sum_numbers = 0
    r = 'Ss'
    while r[0] not in 'Nn':
        number = int(input('Write a numebr: '))
        if count == 0:
            maior = number
            menor = number
            sum_numbers += number
            count += 1
        elif number >= maior:
            maior = number
            sum_numbers += number
            count += 1
        elif number <= menor and number != 0:
            menor = number
            sum_numbers += number
            count += 1
        r = str(input(f'{cores['red']}Deseja continuar?: [S/n]{cores['clean']}'))
    media = sum_numbers / count
    print(f'A média dos valores é: {cores['red']}{media:.2f}{cores['clean']}')
    print(f'O maior valor foi: {cores['red']}{maior}{cores['clean']}')
    print(f'O menor valor foi: {cores['green']}{menor}{cores['clean']}')
maior_menor()