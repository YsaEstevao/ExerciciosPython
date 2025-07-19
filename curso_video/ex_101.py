#Crie um programa que tenha uma função chamada voto() que vai
#receber como parâmetro o ano de nascimento de uma pessoa, retornando
#um valor literal indicando se uma pessoa tem voto negado,opcional
# ou obrigatório nas eleições


def voto(a):
    idade = 2025 - a
    if idade <= 18:
        print(f'Com {idade} anos: Voto Negado!')
    if idade >= 18 and idade < 65:
        print(f'Com {idade} anos: Voto Obrigatório!')
    if idade > 65:
        print(f'Com {idade} anos: Voto Opcional!')

idade = int(input('Ano de Nascimento: '))
voto(idade)
