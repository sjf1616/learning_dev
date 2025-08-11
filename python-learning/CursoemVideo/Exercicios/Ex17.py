from math import hypot

co = float(input('Digite o catato oposto: '))
ca = float(input('Digite o cateto adjacente: '))

hi = hypot(co, ca)

print(f'A hipotenusa é: {hi:.2f}')