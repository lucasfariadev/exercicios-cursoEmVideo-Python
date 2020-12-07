import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mO site pudim não está acessível no momento\033[m')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(site.read())
