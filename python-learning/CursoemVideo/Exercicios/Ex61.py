def prog_aritimetica():
    first = int(input('Write first term: '))
    reason = int(input('Write the reason: '))
    term = first
    i = 1
    while i <= 10:
        print(f'{term}', end=' -> ')
        term += reason
        i += 1
    print('ACABOU')

prog_aritimetica()