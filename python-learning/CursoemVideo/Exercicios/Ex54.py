import random
import numpy as np
import datetime

def verifica_maior_idade():
    total_maioridade = 0
    total_menoridade = 0
    idades = np.array([])
    for i in range(0, 7+1):
        idade = random.randint(1980, 2025)
        idade = datetime.date.today().year - idade
        if idade >= 18:
            total_maioridade += 1
            idades = np.append(idades, [idade])
        else:
            total_menoridade += 1
            idades = np.append(idades, [idade])
    print(f'O total de maior idade é \033[31m{total_maioridade}\033[m')
    print(f'O total de menor idade é \033[31m{total_menoridade}\033[m')
    print(f'A idades adicionadas foram: {idades}')

verifica_maior_idade()
