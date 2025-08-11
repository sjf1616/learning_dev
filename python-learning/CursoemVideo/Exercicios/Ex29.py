s=int(input('Digite a velocidade:'))
if s > 80:
    multa = ( s - 80) * 7
    print(f'Você passou a {s}Km/h, a multa irá custar R${multa:.2f}')