lanche= 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
#for comida in lanche:
#    print(f'EU vou comer {comida}')
#print(f'Comi para caramba')

for cont in range(0, len(lanche)):
    print(f'{lanche[cont]}')

for en, lan in enumerate(lanche):
    print(f'Eu vou comer {lan} na posição {en}')