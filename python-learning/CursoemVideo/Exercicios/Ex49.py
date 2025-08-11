def tabuada_v2():
    n = int(input('Digite um número: '))
    for i in range(0, 10+1):
        print(f'\033[32m{n}\033[m X \033[32m{i}\033[m = \033[31m{n * i}\033[m')

tabuada_v2()