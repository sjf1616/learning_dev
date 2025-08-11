nome = str(input('What is your name?'))

#Estrutura condicional aninhada
if nome == 'Samuel':
    print(f'Que nome mais bonito')
elif nome == 'Pedro'or nome == 'Maria' or nome== 'Paulo':
    print(f'Seu nome é bem comum no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print(f'Belo nome feminino')
else:
    print(f'Seu nome é bem normal')
print(f'Tenha um bom dia {nome}')