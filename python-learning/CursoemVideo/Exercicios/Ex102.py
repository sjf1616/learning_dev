def fatorial(num, show=False):
    i = num - 1
    if show:
        print(f'{num}', end=' - ')
        while i > 0:
            num *= i
            print(f'{i}', end=' - ')
            i -= 1
        print(num)
    else:
        while i > 0:
            num *= i
            i -= 1
        print(f'Total do número fatorial é: {num}')


n = int(input('Numero fatorial: '))
fatorial(n, True)