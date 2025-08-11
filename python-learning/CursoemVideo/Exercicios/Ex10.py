carteira = float(input('Quando dinheiro há na sua carteira?: '))
dolar = 6.21

compra = carteira / dolar

print(f'Ele poderá complrar US$\033[32m{compra:.2f}\033[m')