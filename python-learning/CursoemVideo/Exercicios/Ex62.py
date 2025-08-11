def prog_aritimetica():
    cor = {'Clean': '\033[m',
           'Red': '\033[31m',
           'Green': '\033[32m'}
    f = ''
    while f != '0':
        first = int(input('Write the first term: '))
        reason = int(input('Write the reason: '))
        term = first
        c = 1
        while c <= 10:
            print(f'{term}', end=' -> ')
            term += reason
            c += 1
        print('ACABOU')
        print(f'\n{cor['Red']}Digite{cor['Clean']} {cor['Green']}"0"{cor['Clean']} {cor['Red']}para finalizar o programa{cor['Clean']}')
        f = str(input('Deseja mostrar outro termo?: '))
    print(f'{cor['Red']}Programa encerrado!')
prog_aritimetica()