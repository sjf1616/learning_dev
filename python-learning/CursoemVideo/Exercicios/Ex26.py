word = str(input('Digite uma frase: ')).strip().upper()

print(f'''
Aparece {word.count('A')} A (s) na frase,
O primeiro A aparece na posição {word.find('A')+1},
O último A aparece na posição {word.rfind('A') + 1}
''')

