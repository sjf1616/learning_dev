def person_analytics():
    hight_year = 0
    total_mens = 0
    mulheres_menos_20 = 0
    while True:
        years_old = int(input('Qual a sua idade?: '))
        sexo = str(input('Qual é o seu sexo: ')).lower().strip()
        if years_old >= 18:
            hight_year += 1
        if sexo.startswith('m'):
            total_mens += 1
        if sexo[0] in 'f' and years_old < 20:
            mulheres_menos_20 += 1

        p = str(input('\033[31mDeseja continuar?: \033[m')).lower().strip()
        if p[0] in 's':
            pass
        elif p[0] in 'n':
            break
    print(f'O total de pessoas maior de 18 anos é: {hight_year}')
    print(f'O total de homens cadastrados foi: {total_mens}')
    print(f'O total de mulheres com menos de 20 anos foi: {mulheres_menos_20}')

person_analytics()