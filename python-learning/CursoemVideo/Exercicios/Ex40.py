n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

m = (n1 + n2) / 2
if m <= 5.0:
    print(f'\033[31mReprovado')
elif m <= 6.9:
    print(f'\033[34mRecuperação')
else:
    print(f'\033[32mAprovado')