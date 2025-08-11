metros = int(input('Quantos metros você gostaria de calcular: '))
cm = metros * 100
mm = cm * 10
print(f'''\033[32m{metros}m\033[m em CM é: \033[32m{cm}cm\033[m, e em MM é: \033[32m{mm}mm\033[m''')