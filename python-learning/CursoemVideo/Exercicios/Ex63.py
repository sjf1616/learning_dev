def fibonacci():
    term = int(input('Write a anything number: '))
    t1 = 0
    t2 = 1
    print(f'{t1} -> {t2}', end='')
    count = 3
    while count <= term:
        t3 = t1 + t2
        print(f' -> {t3}', end='')
        t1 = t2
        t2 = t3
        count += 1
fibonacci()