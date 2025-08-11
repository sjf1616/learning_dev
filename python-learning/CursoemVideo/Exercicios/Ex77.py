def contando_vogais():
    vogal = 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'
    palavras = 'Amo meu amor', 'Chocolate é bom', 'Quero Pizza'

    total_vogal = 0

    for palavra in palavras:
        print(f'\n{palavra}: ', end='')
        for letra in palavra:
            if letra in vogal:
                print(f'{letra}', end=' - ')
                total_vogal += 1
        print(f'Fim')
    print(f'\nO total de vogal é: {total_vogal}')


contando_vogais()