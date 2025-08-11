import numpy as np
import random

def pesos():
    total_pesos = np.array([])
    for i in range(0, 5+1):
        peso = random.randint(65, 110)
        total_pesos = np.append(total_pesos, peso)

    print(f'O maior peso registrado foi \033[31m{np.max(total_pesos)}\033[m')
    print(f'O menor peso registrado foi \033[32m{np.min(total_pesos)}\033[m')


pesos()