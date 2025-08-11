sal=float(input('Digite o seu salário: '))

if sal <= 1250:
    aumento = ( sal * 15 ) / 100
    sal_aumento = sal + aumento
    print(f'O salário de {sal} teve um aumento de {aumento} e ficou {sal_aumento} ')
else:
    aumento = ( sal * 10 ) / 100
    sal_aumento = sal + aumento
    print(f'O salário de {sal} teve um aumento de {aumento} e ficou {sal_aumento} ')