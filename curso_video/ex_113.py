
def leiaInt(n):
    num = input(n)
    try:
        num.isnumeric() == True
        num = int(num)
    except:
        print('ERROR! Digite um número inteiro válido!')
        leiaInt(n)
    else: 
        num2 = leiaFloat('Digite um número Real: ')
        print(f'O valor inteiro foi {num} e o real foi {num2}')


def leiaFloat(n):
    num2 = input(n)
    try:
        num2 = float(num2)
        return num2
    except (ValueError,TypeError):
        if num2 == '':
            num2 = 0
            return num2
        else:
            print('ERROR! Digite um número Real válido: ')
            return leiaFloat(n)

valor = leiaInt('Digite um número Inteiro: ')
