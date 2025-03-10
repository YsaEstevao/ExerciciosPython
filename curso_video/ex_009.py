#68) Crie um programa que leia sexo e peso de 8 pessoas, usando a estrutura
#“para”. No final, mostre na tela:
#a) Quantas mulheres foram cadastradas
#b) Quantos homens pesam mais de 100Kg
#c) A média de peso entre as mulheres
#d) O maior peso entre os homens

maior_homem = 0
mulheres = 0
homem_cem = 0
media_mulheres = 0
maior_peso = 0

for c in range(0,8):
    sexo = input('Digite seu genero: ')
    peso = int(input("digite seu peso: "))
    if sexo == 'feminino':
        mulheres += 1
        media_mulheres = media_mulheres + peso
    if sexo == 'masculino' and maior_peso < peso:
        maior_peso = peso
    if sexo == 'masculino' and peso >= 100:
        homem_cem += 1


print('Foram cadastradas {} mulheres\n{} homens pesam mais de cem quilos\nA media de peso das mulheres é {}\nO maior peso entre os homens é {}'.format(mulheres,homem_cem,media_mulheres/mulheres,maior_peso))

