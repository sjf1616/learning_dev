def tabuadav3():
    while True:
        print(f'Para finalizar coloque um número negativo')
        number = int(input('Write a number: '))
        if number <= -1:
            break
        for i in range(0, 11):
            print(f'{i} x {number} = {i * number}')
    print(f'Calculadora finalizada')
tabuadav3()