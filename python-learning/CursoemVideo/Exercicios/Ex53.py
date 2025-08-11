def eh_palindromo(x):
    if x == x[::-1]:
        return True
    else:
        return False


frase = str(input('Digite um palindromo: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)

if eh_palindromo(junto):
    print(f'A frase {frase} é um palindromo')
else:
    print(f'A frase {frase} não é um palindromo')