#for c in range(1, 10):
    #print(c)
#print(f'FIM')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print(f'\033[31mPrograma encerrado\033[m')