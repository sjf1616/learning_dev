def voto(x):
    from datetime import date

    i = date.today().year - x
    if i < 16:
        return 'NEGADO'
    elif i < 18 or i >= 65:
        return 'OPCIONAL'
    else:
        return  'OBRIGATÓRIO'


n = int(input('Qual seu ano de nascimento?: '))
resposta = voto(n)
print(f'Você nasceu em {n}, seu voto é: {resposta}')