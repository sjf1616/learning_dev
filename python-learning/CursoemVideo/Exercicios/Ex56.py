def perfil():
    years_older = 0
    name_than_older = ''
    media_years_old = 0
    more_girls_twelve_years = 0

    for i in range(0, 4+1):
        name = str(input('Digite o nome: '))
        idade = int(input('Digite a idade: '))
        sexo = str(input('Digite o Sexo: M ou F: '))
        if sexo in 'Mn':
            if idade > years_older:
                years_older = idade
                name_than_older = name
                media_years_old += idade
            else:
                media_years_old += idade
        elif sexo in 'Ff':
            if idade <= 20:
                media_years_old += idade
                more_girls_twelve_years += 1
            else:
                media_years_old = idade


    print(f'A média de idade foi: {media_years_old / 4}')
    print(f'O nome do homem mais velho é {name_than_older}')
    print(f'O total de mulheres com menos de 20 anos é: {more_girls_twelve_years}')

perfil()