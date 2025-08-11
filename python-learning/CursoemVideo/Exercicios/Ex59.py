from time import sleep

def calculadora():
    sair_calculadora = 0
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    while sair_calculadora != 5:
        menu = int(input('''
-------------------------
[ 1 ] - Somar
[ 2 ] - Multiplicar
[ 3 ] - Maior
[ 4 ] - Novos números
[ 5 ] - Sair do programa
-------------------------\n\n'''))
        if menu == 1:
            print(f'Resultado: \033[32m{n1} + {n2}\033[m = \033[34m{n1 + n2}\033[m\n')
            sleep(1)
        elif menu == 2:
            print(f'Resultado: \033[32m{n1} x {n2}\033[m = \033[34m{n1 * n2}\033[m\n')
            sleep(1)
        elif menu == 3:
            if n1 > n2:
                print(f'Resultado: O número \033[32m{n1}\033[m é maior\n')
                sleep(1)
            elif n2 > n1:
                print(f'Resultado: O número \033[32m{n2}\033[m é maior\n')
                sleep(1)
            else:
                print(f'Resultado: O números são iguais\n')
                sleep(1)
        elif menu == 4:
            n1 = int(input('Digite o primeiro valor: '))
            n2 = int(input('Digite o segundo valor: '))
            sleep(1)
        elif menu == 5:
            print(f'\033[31mFinalizando programa', end='')
            for i in range(0, 3):
                print(f'.',end='')
                sleep(0.5)
                sair_calculadora = 5

calculadora()