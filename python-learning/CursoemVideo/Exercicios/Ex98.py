from time import sleep


def contador(i, f, p):

    for _ in range(i, f, p):
        print(f'{_}', end=' ')
        sleep(0.5)
    print('FIM')

print('=-' * 30)
contador(0, 11, 1)
print('=-' * 30)
contador(10, -1, -2)
print('=-' * 30)
print('Agora é sua vez de personalizar a contagem!')
c = int(input('Digite o incio: '))
t = int(input('Digite o fim: '))
pl = int(input('Digite o passo: '))

contador(c, t+1, pl)