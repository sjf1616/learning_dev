def readInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mError: Please, writer a valid number. "Integer"\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mError: User dont want to continue or insert data\033[m')
            return 0
        else:
            return n

def readFloat(msg):
    while True:
        try:
            n = float(input(msg).replace(',','.'))
        except (ValueError, TypeError):
            print(f'\033[31mError: Please, writer a valid number. "Integer"\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mError: User dont want to continue or insert data\033[m')
            return 0
        else:
            return n

valid_number_integer = readInt('Write a válid number integer: ')
valid_number_float = readFloat('Write a válid number float: ')
print(f'O número digita {valid_number_integer} é \033[32mválido\033[m!')
print(f'O número digita {valid_number_float} é \033[32mválido\033[m!')