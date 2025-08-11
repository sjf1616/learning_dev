def syst_help():
    from time import sleep
    color_text = {
        'white':'\033[m',
        'red':'\033[m'
    }
    color_bg = {
        'blue':'\033[97;44m',
        'white':'\033[30;107m',
        'clean':'\033[m',
        'green':'\033[30;42m'
    }

    input_help = ''
    while input_help in 'fim':
        print(f"{color_bg['green']}{'~' * 40}")
        print(f'{'Sistema de Ajuda SystHELP':^40}')
        print(f"{'~' * 40}")

        input_help = str(input(f'{color_bg['clean']}Function or Library: ')).lower().strip()

        print(f"{color_bg['blue']}{'~' * 40}")
        print(f'{'Acesando o manual do comando':^30}{input_help}')
        print(f"{'~' * 40}")
        sleep(0.5)
        print(f'{color_bg['white']}{help(input_help)}')

syst_help()