


def pa():
     pt = int(input('Primeiro termo: '))
     r = int(input('Razão: '))
     for i in range(pt, 20+1, r):
         print(f'{i}', end=' - ')
     print('\033[31mAcabou'.upper())

pa()