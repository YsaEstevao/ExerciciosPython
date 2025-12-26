def metade(n=0):
    return n/2 

def dobro(n=0):
    return n*2

def aumentar(n=0,v=0):
    return (n * (v/100)) + n

def diminuir(n=0, v=0):
    return n - (n*(v/100))

def moeda(n=0,p='R$'):
    return f'{p}{n:.2f}'.replace('.',',')