cores={'limpa':'\033[m',
       'rosa':'\033[35m',
       'verde':'\033[32m'}

v1 = int(input("Digite um valor: "))
v2 = int(input("Digite um segundo valor: "))
s = v1 + v2
print(f'O valor entre {cores['rosa']}{v1} + {v2}{cores['limpa']} é: {cores['verde']}{s}{cores['limpa']}')