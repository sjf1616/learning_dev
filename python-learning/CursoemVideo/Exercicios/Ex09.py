n = int(input('Digite um número: '))

tabuada = 0

for tabuada in range(1, 11):
    valor = n * tabuada
    print(f'\033[35m{n} X {tabuada}\033[m = \033[32m{valor}\033[m')
    tabuada += 1
