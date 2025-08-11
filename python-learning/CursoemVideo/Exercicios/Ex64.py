def tratando_varios_valores():
    cores = {
        'Green':'\033[32m',
        'Clean':'\033[m',
        'Red':'\033[31m'
    }
    flag = 0
    count_numbers = 0
    sum_numbers = 0
    while flag != 999:
        print(f'{cores['Red']}Digite "999" para finalizar o programa!{cores['Clean']}')
        flag = int(input('Write a any number: '))
        count_numbers += 1
        sum_numbers += flag
    sum_numbers -= 999
    count_numbers -= 1
    print(f'Total numbers count: {cores['Green']}{count_numbers}{cores['Clean']}')
    print(f'Sum of all numbers: {cores['Green']}{sum_numbers}{cores['Clean']}')
tratando_varios_valores()