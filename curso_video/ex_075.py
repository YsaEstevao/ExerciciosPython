tupla = ()
c = 0

while c != 4:
    num = int(input('Digite um número: '))
    tupla = tupla + (num,)
    c += 1
c = 0
d = 0
e = 0

for c in range(len(tupla)):
    if tupla[c] == '9':
        d += 1
    if int(tupla[c]) % 2 == 0:
        e += 1

cont = 0
for j in range(len(tupla)):
    if tupla[j] == 3:
        cont = tupla.index(3)
    else:
        cont = 'em nenhuma'


print(f'o numero 9 apareceu {d} vezes')
print(f'o primeiro 3 foi digitado {cont} posição')
print(f'foram digitados {e} numeros pares')





