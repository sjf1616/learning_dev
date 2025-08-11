def caixa_eletronico():
    troco = 1
    c = 0
    v = 0
    d = 0
    u = 0
    while troco != 0:
        valor_saque = int(input('Digite o valor que deseja sacar: '))
        troco = valor_saque

        while troco != 0:
            if troco >= 50:
                c += 1
                troco -= 50
            elif troco >= 20:
                v += 1
                troco -= 20
            elif troco >= 10:
                d += 1
                troco -= 10
            elif troco >= 1:
                u += 1
                troco -= 1

        print(f'''
O total das cédulas de R$ 50,00 foi de {c}
O total das cédulas de R$ 20,00 foi de {v}
O total das cédulas de R$ 10,00 foi de {d}
O total das cédulas de R$ 1,00 foi de {u}''')

caixa_eletronico()