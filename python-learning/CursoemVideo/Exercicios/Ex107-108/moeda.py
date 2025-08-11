def increase(value, add, form=True):
    value = int(value)
    add = int(add)
    if form:
        return  f'R$ {(value + add):.2f}'
    else:
        return value + add

def decrease(value, dim, form=True):
    value = int(value)
    dim = int(dim)
    if form:
        return f'R$ {(value - dim):.2f}'
    else:
        return value - dim

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

def resume(v1, v2=0, form=True):
    print('-' * 30)
    print(f'{'Preços':^30}')
    print('-' * 30)
    print(f'Preço avaliado: {increase(v1, 0, form):.10}')
    print(f'Preço somado: {increase(v1, v2, form):.10}')
    print(f'Preço descontado: {decrease(v1, v2, form):.10}')
    print(f'Preço dobrado: {double(v1, form):.10}')
    print(f'Preço médio: {mean(v1, form):.10}')