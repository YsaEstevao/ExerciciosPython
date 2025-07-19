#crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um dicionario
#e todos os dicionários em uma lista
#no final mostre:
#quantas pessoas foram cadastradas
#a media de idade do grupo
# uma lista com todas as mulheres
#uma lista com todas as pessoas com idade acima da media

escolha = 's'
lista = []
media = 0

while escolha == 's':
    dici = {}
    dici['Nome'] = input('Nome: ')
    dici['Sexo'] = input('Sexo: [M/F] ').upper()
    dici['Idade'] = int(input('Idade: '))
    lista.append(dici)
    media = (media + dici['Idade']) / len(lista)
    escolha = input('Deseja continuar? ')

print(f'-> Foram cadastradas {len(lista)} pessoas')
print(f'-> A média de idade é de {media} anos')
print(f'-> As mulheres cadastradas foram:',end=' ')

for p in lista:
    if p['Sexo'] == 'F':
        print(p['Nome'],end = ' ')
print()
print('-> Lista das pessoas a cima da média: ')
for k in lista:
    if k['Idade'] >= media:
        print('       ', end = '')
        for k,v in p.items():
            print(f'{k} = {v}' end = ' ')

