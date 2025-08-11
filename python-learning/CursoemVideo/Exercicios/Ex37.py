i = int(input('Digite um número decimal: '))
option = int(input('''
1 to Binary
2 to Octal
3 to Hexadecimal\n'''))

if option == 1:
    print(f'\033[31m{bin(i)[2:]}')
elif option == 2:
    print(f'\033[31m{oct(i)[2:]}')
elif option == 3:
    print(f'\033[31m{hex(i)[2:]}')

