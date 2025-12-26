import moeda

p = float(input('Digite o preço: '))
print(f'A medade de {p} é {moeda.metade(p)}\nO dobro de {p} é {moeda.dobro(p)}\nAumentando 10%, temos {moeda.aumentar(p,10)}\nReduzindo 13%, temos {moeda.diminuir(p,13)}')
