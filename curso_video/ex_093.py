#Crie um programa que gerencia o aproveitamento de um jogador de futebol
#O programa vai ler o nome do jogador e quantas partidas ele jogou
#Depois vai ler a quantidade de gols feitos em cada partida
#No final,tudo isso será guardado em um dicionario
#incluindo o total de gols feitos durante o campeonato

aproveitamento = {}

aproveitamento['nome'] = input('Nome do jogador: ')
p = int(input(f'Quantas partidas {aproveitamento['nome']} jogou? '))
gol = []
total = 0

for c in range(0,p):
    g = int(input(f'Quantos gols na partida {c+1}? '))
    total = total + g
    gol.append(g)

aproveitamento['gols'] = gol
aproveitamento['total'] = total
print('-'*20)
print(aproveitamento)
print('-'*20)
for k, v in aproveitamento.items():
    print(f'O campo {k} tem o valor {v}.')
print('-'*20)
print(f'O jogador {aproveitamento["nome"]} jogou {p} partidas.')
for k in range(len(gol)):
    print(f'    => Na partida {k+1}, fez {gol[k]} gols')
print(f'Foi um total de {total} gols.')