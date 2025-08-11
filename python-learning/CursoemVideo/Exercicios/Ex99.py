from time import sleep


def descobre_maior(*num):
    print('-=' * 15)
    print('Analisando os valores passados...')
    for _ in num:
        print(f'{_}', end=' ')
        sleep(0.5)
    print(f'Foram os valores informados')
    print(f'O maior valor informado foi {max(num)}')
    sleep(1.5)

descobre_maior(2, 9, 4, 5, 7, 1)
descobre_maior(4, 7, 8)
descobre_maior(1, 2)
descobre_maior(6)
descobre_maior(0)