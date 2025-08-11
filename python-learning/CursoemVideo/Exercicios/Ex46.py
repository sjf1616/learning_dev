import time

def contagem_regressiva():
    for i in range(10, 0, -1):
        if i >= 5:
            print(f'\033[32m{i}')
            time.sleep(1)
        else:
            print(f'\033[31m{i}')
            time.sleep(1)

contagem_regressiva()