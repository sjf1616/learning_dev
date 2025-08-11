import urllib.request, urllib.error

try:
    site = urllib.request.urlopen("http://pudim.com.br")
except urllib.error.URLError:
    print(f'O site pudim não está acessivel no momento')
else:
    print(f'Consegui acessar o site Pudim com sucesso!')
    print(site.read())
