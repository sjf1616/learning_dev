def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mError: "{entrada}" not is valid!\033[m')
        else:
            valido = True
            return float(entrada)
