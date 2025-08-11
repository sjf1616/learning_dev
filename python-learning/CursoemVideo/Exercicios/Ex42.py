l1 = float(input())
l2 = float(input())
l3 = float(input())

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print(f'É um triangulo')
    if l1 == l2 and l2 == l3 and l1 == l3:
        print(f'É um triangulo EQUILATERO')
    elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
        print(f'É um triangulo ISÓCELES')
    else:
        print(f'É um triangulo ESCALENO')
else:
    print(f'NÃO É UM TRIANGULO')