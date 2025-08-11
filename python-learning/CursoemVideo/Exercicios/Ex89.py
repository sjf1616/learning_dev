def boletim():
    alunos = list()
    boletim = list()

    while True:
        boletim.append(str(input('Nome: ')))
        boletim.append(float(input('Nota 1: ')))
        boletim.append(float(input('Nota 2: ')))
        alunos.append(boletim[:])
        boletim.clear()
        c = str(input('Deseja continuar? [Y/N]: ')).lower().strip()
        while c not in 'YyNn':
            c = str(input('\033[31mResposta Errada! Aceito apenas [Y/N]: \033[m')).lower().strip()
        if c in 'Nn':
            break

    print(f'Lista de alunos')
    for e, i in enumerate(alunos):
        print(f'{e+1} - {i[0]}\nNota 1: {i[1]}\nNota 2: {i[2]}\nMedia Final: {(i[1] + i[2])/2}')

boletim()