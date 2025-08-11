v = float(input('Valor do produto: '))
option=int(input('''
Digite a opção desejada: 
1 - Á vista
2 - Parcelado\n'''))

if option == 1:
    op2 = int(input('''
1 - Dinheiro/Cheque
2 - Cartão\n'''))
    if op2 == 1:
        por = (10 / v) * 100
        print(f'O valor final do produto R$ {v - por:.2f}')
    elif op2 == 2:
        por  = (5 / v) * 100
        print(f'O valor final do produto R$ {v - por:.2f}')
elif option == 2:
    op2 = int(input('Quantas vezes?'))
    if op2 >= 3:
        por= (20 / v) * 100
        print(f'Valor final do produto R$ {v + por:.2f}')
    elif op2 <= 2:
        print(f'O valor do produto continuar o mesmo R$ {v}')