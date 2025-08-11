l = int(input('Qual é a largura da parede em metros?: '))
a = int(input('Qual é a altura da parede em metros?: '))

a = l * a

qtd_tinta = a / 2

print(f'A quantidade de tintas necessarias para pintar a parede com o tamanho de {a}m² é {qtd_tinta} litros')