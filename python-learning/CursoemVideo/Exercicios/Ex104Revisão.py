
def readInt(msg):
    check = False
    value = 0
    while True:
        number = str(input(msg))
        if number.isnumeric():
            value = int(number)
            check = True
        else:
            print(f'\033[0;31mERROR! You do not write a numeric, check is {check}\033[m')
        if check:
            break
    return value

number = readInt('Write a valid number: ')
print(f'You write a valid number: \033[0;35m{number}\033[m')