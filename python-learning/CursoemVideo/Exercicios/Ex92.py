from datetime import date

def cadastro_trabalhador():
    cadastro = dict() #Criando dicionario

    # Lendo nome, data de nascimento, ctps
    nome = str(input(('Nome: ')))
    nascimento = int(input('Ano nascimento: '))
    ctps = int(input('CTPS: '))

    # Buscando a data atual
    atual = date.today().year

    # Filtrando a idade
    idade = atual - nascimento

    #Adicionando ao dicionario
    cadastro['nome'] = nome
    cadastro['nascimento'] = nascimento
    cadastro['ctps'] = ctps
    cadastro['idade'] = idade

    # Adicionando Ano contrato e Salario caso CTPS for diferente de 0
    if ctps != 0:
        ano_contrato = int(input('Ano contrato: '))
        salario = float(input('Salário: '))
        cadastro['contrato'] = ano_contrato
        cadastro['salario'] = salario

        # Buscando a idade quando foi contratado
        idade_contrato = atual - ano_contrato
        aposentar = idade_contrato + 35

        # Colocando na tela os dados do cadastro
        for k, v in cadastro.items():
            print(f'{k} = {v}')

        print(f'O {cadastro['nome']} irá se aposentar com {aposentar} anos')

    else:
        # Colocando na tela os dados do cadastro
        for k, v in cadastro.items():
            print(f'{k} = {v}')

        print(f'O {cadastro['nome']} só irá se aposentar após 35 anos e contribuição')

cadastro_trabalhador()
