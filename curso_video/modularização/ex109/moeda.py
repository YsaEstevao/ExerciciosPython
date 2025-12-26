
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