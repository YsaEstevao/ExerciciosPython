galera = []
dado = []
leve = []
escolha = 's'
c = 0

while escolha == 's':
    dado.append(input('Nome: '))
    dado.append((int(input('Peso: '))))
    galera.append(dado[:])
    dado.clear()
    c += 1
    escolha = input('Deseja continuar? S/N')


for p in galera:
    if 

print(f'vc cadastrou {c} pessoas')