#crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante á função input(0 do python.
#Só que fazendo a validação para aceitar somente valores numericos
# EX: n = leiaint('Digite um n')
'\033[0;31mDigite um valor\033[m'

def leiaInt(n):
    a = input(n)
    if a.isnumeric():
        a = int(a)
        print(f'Você acabou de digitar o número {a}')
    else:
        while type(a) != int():
            print('\033[1;31mError! Digite um número inteiro vàlido.\033[m')
            a = input(n)
            if a.isnumeric():
                a = int(a)
                print(f'Voce acabou de digitar o numero {a}.')
                break



n = leiaInt('Digite um número: ')