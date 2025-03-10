ano = 0
idade = 0
maior = 0
menor = 0
atual = 2024

for c in range (0,7):
    ano = int(input('digite seu ano de nascimento'))
    atual = atual - ano
    if atual >= 18:
        maior += 1
    else:
        menor += 1

print('a menor idade é {}, a maior idade é {}'.format(menor,maior))


