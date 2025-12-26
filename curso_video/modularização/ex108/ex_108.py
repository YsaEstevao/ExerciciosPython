from ex108 import moeda

p = float(input("Digite o preço: R$"))
print(f'A medade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}\nO dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}\nAumentando 10%, temos {moeda.moeda(moeda.aumentar(p,10))}\nReduzindo 13%, temos {moeda.moeda(moeda.diminuir(p,13))}')
