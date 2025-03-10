#crie um programa onde o usuário possa digitar cinco valores numericos
#e cadastre-os em uma lista,ja na posição correta de inserção
#(sem usar sort())

lita = []
ultimo = True

for i in range(0,5):
    valor = int(input(f'Digite o {i+1} valor:'))
    if i == 0:
        lita.append(valor)
    if i >= 1:
        for lugar, dentro in enumerate(lita):
            if valor < dentro:
                lita.insert(lugar,valor)
                ultimo = False
                break
        if ultimo == True:
            lita.append(valor)
        ultimo = True

print(lita)