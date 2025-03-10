grupo = []
escolha = 's'

while escolha == "s":
    valor = int(input('Digite um valor: '))
    if valor in grupo:
        print('Valor não permitido!')
    else:
        grupo.append(valor)
        escolha = input('Deseja continuar? [S/N]')

grupo.sort()
print(f'os valores digitados foram: {grupo}')