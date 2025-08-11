def increase(value, percent , form=True):
    value = int(value)
    percent = int(percent)
    porcentagem = (percent * value) / 100
    soma = value + porcentagem
    if form:
        return  f'R$ {soma:.2f}'
    else:
        return soma

def decrease(value, percent, form=True):
    value = int(value)
    percent = int(percent)
    porcentagem = (percent * value) / 100
    soma = value - porcentagem
    if form:
        return f'R$ {soma:.2f}'
    else:
        return soma

def  double(value, form=True):
    value = int(value)
    if form:
        return f'R$ {(value * 2):.2f}'
    else:
        return value * 2

def mean(value, form=True):
    value = int(value)
    if form:
        return f'R$ {(value / 2):.2f}'
    else:
        return value / 2

def resume(v1, v2=0, v3=0, form=True):
    print('-' * 30)
    print(f'{'Preços':^30}')
    print('-' * 30)
    print(f'Preço analisado: {increase(v1, 0, form):.10}')
    print(f'Dobro do preço: {double(v1, form):.10}')
    print(f'Metade do preço: {mean(v1, form):.10}')
    print(f'{v2}% de aumento: {increase(v1, v2, form):.10}')
    print(f'{v3}% de redução: {decrease(v1, v3, form):.10}')
    print('-' * 30)
