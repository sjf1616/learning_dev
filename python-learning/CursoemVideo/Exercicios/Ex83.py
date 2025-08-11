def validando_expressao():
    aberto = list()
    fechado = list()
    expressao = str(input('Digite uma expressão: '))
    for l in expressao:
        if l in '(':
            aberto.append('(')
        elif l in ')':
            fechado.append('(')
    if len(aberto) == len(fechado):
        print(f'É uma expressão válida')
    else:
        print(f'A expressão não é válida')
validando_expressao()