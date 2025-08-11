def factorial():
    n = int(input('Digite um número inteiro: '))
    i = n

    while True:
        if i == 1:
            break
        i -= 1
        n *= i
        print(f'{i}', end=' x ' if i > 1 else ' = ')
    print(n)

factorial()