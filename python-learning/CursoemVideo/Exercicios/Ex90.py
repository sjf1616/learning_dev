
def dicionario():
    boletim = dict()

    boletim['nome'] = str(input('Nome do aluno: '))
    boletim['nota1'] = float(input('Digite a primeira nota: '))
    boletim['nota2'] = float(input('Digite a segunda nota: '))

    soma_notas = 0

    for k, v in boletim.items():
        if k == 'nota1' or k == 'nota2':
            soma_notas += v

    media = soma_notas / 2

    boletim['media'] = media
    if media <= 5:
        boletim['Situação'] = 'Reprovado'
    elif media <= 7:
        boletim['Situação'] = 'Recuperação'
    else:
        boletim['Situação'] = 'Aprovado'

    print(f'=' * 20)
    print(f'Boletim')
    for k, v in boletim.items():
        print(f'{k} aluno: {v}')

dicionario()