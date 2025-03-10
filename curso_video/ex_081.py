lista = []
c = 0
escolha = 's'

while escolha == 's':
    valor = int(input('digite um valor:'))
    if c == 0:
        lista.append(valor)
    elif valor < lista[-1]:
        lista.append(valor)
    else:
        posi = 0
        while posi < len(lista):
            if valor >= lista[posi]:
                lista.insert(posi,valor)
                break
            posi += 1
    escolha = input('Deseja continuar? S/N')
    c+=1

cinco = 'não está'
for j in lista:
    if 5 in lista:
        cinco = 'está'

print(f'Foram digitados {c} números\nA lista decrescente fica {lista}\nO numero 5 {cinco} na lista')