n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = ( n1 + n2 ) / 2

cores={'limpar':'\033[m',
       'vermelho':'\033[31m',
       'verde':'\033[32m',
       'amarelo':'\033[33m'}

print(f'A média é : {media}')

if media >= 7:
    print(f'{cores['verde']}Passou de ano{cores['limpar']}')
elif media >= 5:
    print(f'{cores['amarelo']}Recuperação{cores['limpar']}')
else:
    print(f'{cores['vermelho']}Reprovado{cores['limpar']}')