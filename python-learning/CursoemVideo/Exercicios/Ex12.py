p = float(input('Qual o preço do produto?: '))

desconto = ( 5 / 100 ) * p

total = p - desconto

print(f'O valor do produto com desconto é R$ {total}')