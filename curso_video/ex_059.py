n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
somar = 0
multiplicar = 0
maior = 0
nonum = 0
sair = 0

while sair != 5:
    sair = int(input('Qual operação deseja fazer?\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos numeros\n[5] sair do programa '))
    if sair == 1:
        print(n1+n2)
    if sair == 2:
        print(n1*n2)
    if sair == 3:
        if n1 > n2:
            print(n1)
        else:
            print(n2)
    if sair == 4:
        n1 = int(input('digite um numero: '))
        n2 = int(input('digite outro numero: '))
