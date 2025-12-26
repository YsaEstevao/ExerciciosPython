

def metade(n=0,p=True):
    n = n/2
    if p == True:
        return f'R${n:.2f}'.replace('.',',')
    else:
        return n

def dobro(n=0, p = True):
    n = n*2
    if p == True:
        return f'R${n:.2f}'.replace('.',',')
    else:
        return n


def aumentar(n=0,v=0, p = True):
    n = (n * (v/100)) + n
    if p == True:
        return f'R${n:.2f}'.replace('.',',')
    else:
        return n
def diminuir(n=0, v=0, p = True):
    n = n - (n*(v/100))
    if p == True:
        return f'R${n:.2f}'.replace('.',',')
    else:
        return n

def moeda(n=0,p='R$'):
    return f'{p}{n:.2f}'.replace('.',',')

def resumo(n=0, a=0 ,d=0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço análisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n)}')
    print(f'Metade do preço: \t{metade(n)}')
    print(f'Aumentando {a}% temos: \t{aumentar(n,a)}')
    print(f'Diminuindo {d}% temos: \t{diminuir(n,d)}')
    print('-'*30)