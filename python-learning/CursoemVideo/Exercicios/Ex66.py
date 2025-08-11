def stop_program():
    color = {
        'clean':'\033[m',
        'red':'\033[31m',
        'green':'\033[32m'
    }
    total_number = s = 0
    while True:
        print(f'{color['red']}Para finalizar o programa, digite "999"{color['clean']}')
        number = int(input('Digite um valor: '))
        if number == 999:
            break
        s += number
        total_number += 1
    print(f'O total de números digitados foram: {color['green']}{total_number}{color['clean']}')
    print(f'A soma dos números foi: {color['green']}{s}{color['clean']}')

stop_program()