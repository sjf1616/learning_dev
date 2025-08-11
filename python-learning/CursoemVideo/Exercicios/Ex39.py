import datetime

year = int(input('Digite o ano de nascimento: '))
today = datetime.date.today().year

if today - year == 18:
    print(f'Ano de alistamento')
elif today - year  <= 17:
    print(f'Muito novo para alistar')
    idade = today - year
    faltante = 18 - idade
    print(f'Faltam {faltante} anos')
elif today - year >= 18:
    print(f'Já passou do alistamento')
    i = today - year
    p = i - 18
    print(f'Passou {p} anos')

