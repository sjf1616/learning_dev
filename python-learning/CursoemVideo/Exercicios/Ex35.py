l1 = float(input('Digite a primeira linha: '))
l2 = float(input('Digite a segunda linha: '))
l3 = float(input('Digite a terceira linha:'))

if l1 < l2 + l3 and l1 < l3 + l2 and l2 < l3 + l1:
    print(f'É um triangulo')
else:
    print(f'Não é um triangulo')

