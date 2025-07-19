#Crie um programa que tenha a função fatorial() que receba dois
#parametros: o primeiro que indique o numero a calcular e o outro
#chamado show que será um valor lógico (opcional), indicando se será mostrado
# ou não na tela o processo do calculo do fatorial

def fatorial(a = 1, show = False):
    """
    -> Calcular o fatorial de um numero
    :param a: Valor a ser calculado
    :param show: mostrar a conta (opcional)
    :return: resultado do fatorial
    """
    f = 1
    for c in range(a,0,-1):
        f*=c
        if show == True:
            print(f'{c} ',end = '')
            if c > 1:
                print('x',end=' ')
            else:
                print(f'= {f} ')
    return f

num = int(input('Numero: '))

fatorial(num,)
valor = fatorial(num)
print(valor)
help(fatorial)