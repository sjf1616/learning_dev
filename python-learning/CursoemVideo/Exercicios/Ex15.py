km = int(input('Total KM percorrido: '))
dias = int(input('Total Dias: '))

dias_alugado = dias * 60
km_rodado = km * 0.15

total_pagar = dias_alugado + km_rodado

print(f'O valor a pagar por KM rodado é de R$ {km_rodado}\n'
      f'O valor a pagar por DIAS alugado é de R$ {dias_alugado}\n'
      f'O total ficaria R$ {total_pagar}')