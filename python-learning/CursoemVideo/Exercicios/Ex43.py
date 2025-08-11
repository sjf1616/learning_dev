p = float(input('Qual o seu peso: '))
a = float(input('Qual sua altura em M: '))

imc = p / (a ** 2)

if imc <= 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso Ideal')
elif imc <= 30:
    print(f'Sobrepeso')
elif imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade Mórbida')