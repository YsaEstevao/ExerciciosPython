a = []

for c in range(0,5):
    a.append(int(input('Digite um valor: ')))

for c in range(len(a)):
    aposi = a[c]
    if c == 0:
        menor = aposi
        maior = aposi
    if aposi > maior:
        maior = aposi
    if aposi < menor:
        menor = aposi
print(f'o maior valor digitado foi {maior} na posição {(a.index(maior)+1)} e o menor valor foi {menor} na posição {(a.index(menor)+1)}')