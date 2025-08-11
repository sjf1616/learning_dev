n1=int(input(f'Digite o primeiro número: '))
n2=int(input(f'Digite o segundo número: '))
n3=int(input(f'Digite o terceiro número: '))

if n1 > n2 and n3:
    print(f'O primeiro número é maior, sendo o número {n1}')
else:
    if n2 > n3:
        print(f'O segundo número é maior, sendo o número {n2}')
    else:
        print(f'O terceiro número é maior, sendo o número {n3}')
