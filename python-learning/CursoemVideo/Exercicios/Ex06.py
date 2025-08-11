n = int(input("Digite um número:"))
dobro = n * 2
triplo = n * 3
rq = n ** (1/2)

cores={'vermelho':'\033[31m',
       'verde':'\033[32m',
       'limpar':'\033[m'}


print(f"""O número digitado foi : {cores['vermelho']}{n}{cores['limpar']}
O dobro de {cores['vermelho']}{n}{cores['limpar']} é {cores['verde']}{dobro}{cores['limpar']}
O triplo de {cores['vermelho']}{n}{cores['limpar']} é {cores['verde']}{triplo}{cores['limpar']}
A Raiz Quadrada de {cores['vermelho']}{n}{cores['limpar']} é {cores['verde']}{rq:.2f}{cores['limpar']}""")