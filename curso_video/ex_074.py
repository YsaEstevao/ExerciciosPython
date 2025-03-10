from random import randint

ale = (randint(0,10), randint(0,10),randint(0,10),randint(0,10),randint(0,10))

for c in range(len(ale)):
    maior = ale[0]
    menor = ale[0]
    if ale[c] > maior:
        maior = ale[c]
    if ale[c] < menor:
        menor = ale[c]
print(ale)
print(maior,menor)