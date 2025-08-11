def readInteger(numeric):
    if numeric.isnumeric():
        print(f'Is a numeric')
    else:
        print(f'Is an string')


input_number = input('Write a any number: ')
readInteger(input_number)