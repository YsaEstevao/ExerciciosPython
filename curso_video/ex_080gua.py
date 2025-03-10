lista = []
for c in range (0,5):
    n = int(input('digite um valor: '))
    if c == 0:
        lista.append(n)
    elif n > lista[-1]:
        lista.append(n)
    else:
        posi = 0
        while posi < len(lista):
            if n <= lista[posi]:
                lista.insert(posi,n)
                break
            posi += 1
print(lista)