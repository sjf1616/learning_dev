def unindo_dict_list():
    pessoa = dict()
    pessoas = list()
    mulheres = list()
    acima_media = list()


    while True:
        nome = str(input('Nome: '))
        sexo = str(input('Sexo: '))[0].lower().strip()
        idade = int(input('Idade: '))
        pessoa['Nome'] = nome
        pessoa['Sexo'] = sexo
        pessoa['Idade'] = idade
        pessoas.append(pessoa.copy())

        c = str(input('Deseja continuar?[S/N]: '))[0].lower().strip()
        while c not in 'sn':
            c = str(input('\033[31mRespostas aceita: S=SIM, N=NÃO: \033[m'))[0].lower().strip()
        if c in 'n':
            break

    total_idaide = 0
    media = 0
    for p in pessoas:
        total_idaide += p['Idade']
        media = total_idaide / len(pessoas)

        if p['Sexo'] in 'f':
            mulheres.append(p.copy())

        if p['Idade'] >= media:
            acima_media.append(p.copy())

    print(f'O total de pessoas cadastradas foram: {len(pessoas)}')
    print(f'A média de idade é: {media}')
    print(f'As mulheres são: {mulheres}')
    print(f'As pessoas acima da média são {acima_media}')
unindo_dict_list()