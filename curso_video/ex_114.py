import urllib.request


try:
    site = urllib.request.urlopen('https://pudim.com.br/')
    print('O site pudim ESTÁ acessível!')
except urllib.error.URLError:
    print('O site pudim NÃO está acessível!')
