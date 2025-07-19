#faça um progrmama que tenha uma função chamada ficha(), que receba dois parametros opcionais
#o nome de um jogador e quantos gols ele marcou
#o progmrama deverar ser capaz e mostrar a ficha do jogador, mesmo que algum dado n tenha sido informado corretamente

def ficha(a = '<desconhecido>', b = 0):
    print(f'O jogador {a} fez {b} gol(s) no campeonato.')


n = input('Nome do jogador: ')
g = str(input('Número de gols: '))

if g.isalnum():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(b=g)
else:
    ficha(n,g)