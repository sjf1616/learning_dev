cores={'limpa':'\033[m',
       'verde':'\033[32m'}

valor = input('Digite algo: ')
print(type(valor))
print(f'''
Sò tem espaço?: {cores['verde']}{valor.isspace()}{cores['limpa']}
É um número?: {cores['verde']}{valor.isnumeric()}{cores['limpa']}
É alfabético?: {cores['verde']}{valor.isalpha()}{cores['limpa']}
Está em maiúsculo?: {cores['verde']}{valor.isupper()}{cores['limpa']}
Está em minúsculo?: {cores['verde']}{valor.islower()}{cores['limpa']}
Está captalizado?: {cores['verde']}{valor.istitle()}{cores['limpa']}''')