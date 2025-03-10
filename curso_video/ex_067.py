from random import randint
pc_num = 0
u_num = 0
u_escolha = 0
vit_u = 0
soma = 0

while True:
    pc_num = randint(0,10)
    u_num = int(input('digite um numero:'))
    u_escolha = int(input('Escolha:\n[1] Impar\n[2] Par '))
    if u_escolha == 1:
        soma = u_num + pc_num
        if soma %3 == 0:
            print(f'o computador escolheu {pc_num}\n usuário escolheu {u_num}\nusuario venceu!')
            vit_u += 1
        else:
            print(f'o computador escolheu {pc_num}\n usuário escolheu {u_num}\nusuario perdeu!')
            break
    if u_escolha == 2:
        soma = u_num + pc_num
        if soma %2==0:
            print(f'o computador escolheu {pc_num}\n usuário escolheu {u_num}\nusuario venceu!')
            vit_u += 1
        else:
            print(f'o computador escolheu {pc_num}\n usuário escolheu {u_num}\nusuario perdeu!')
            break
