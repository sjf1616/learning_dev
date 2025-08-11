def verifica_sexo():
    r = ' '
    while r[0] != 'MF':
        r = str(input('Digite o sexo: ')).upper()
        if r == 'M':
            print(f'\033[34mBem Vindo!\033[m')
        elif r == 'F':
            print(f'\033[34mBem Vinda!\033[m')
        else:
            print(f'\033[31mValor errado! Tente novamente\033[m')
verifica_sexo()