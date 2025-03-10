lista = []
par = []
impar = []
escolha = 's'

while escolha == 's':
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    escolha = input('Deseja continuar? S/N')
print(f'a lista que vc digitou foi {lista}\na lista com os pares são {par}\na lista com os impares são {impar}')