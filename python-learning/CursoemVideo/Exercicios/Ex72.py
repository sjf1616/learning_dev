def number_to_extensive():
    numbers = ( 'zero','um', 'dois', 'três', 'quatro',
                'cinco','seis', 'sete', 'oito',
                'nove', 'dez', 'onze', 'doze',
                'treze', 'quatorze', 'quinze',
                'dezesseis', 'dezessete', 'dezoito',
                'dezenove', 'vinte' )

    n = int(input('Writhe a number to print: '))
    print(f'O número \033[31m{n}\033[m por extenso é \033[32m{numbers[n]}\033[m')

number_to_extensive()