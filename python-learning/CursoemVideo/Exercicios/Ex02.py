cores={'vermelho':'\033[31m', 'limpa':'\033[m'}

nome = input(str('Qual é o seu nome?: '))
print(f'Seu nome é: {cores['vermelho']}{nome}{cores['limpa']}')