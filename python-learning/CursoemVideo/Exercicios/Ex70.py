def mercado():
    carrinho = 0
    maior_mil = 0
    name_product = ''
    menor_valor = 0
    while True:
        name = str(input('Qual o nome do produto: ')).lower().strip()
        price = float(input('Qual é o preço: '))
        carrinho += price
        if menor_valor == 0 or price < menor_valor:
            menor_valor = price
            name_product = name
        if price >= 1000:
            maior_mil += 1

        p = str(input('Deseja continuar?: ')).lower().strip()
        if p.startswith('s'):
            pass
        else:
            break
    print(f'O total gasto na compra foi de: {carrinho:.2f}')
    print(f'O total de produtos com valor maior de R$ 1000,00 é {maior_mil}')
    print(f'O produto com o menor valor é o {name_product}')
mercado()


