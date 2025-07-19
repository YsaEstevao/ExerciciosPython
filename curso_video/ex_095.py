
escolha = 's'
tudo = []
while escolha == 's':
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
    tudo.append(aproveitamento)
    escolha = input('Deseja continuar? s/n ')
    print('-'*30)
print(tudo)
print('-'*30)
print('cod      Nome        gols         total  ')

c = 0
for k in tudo:
    print(f'{c}         {k["nome"]}          {k["gols"]}         {k["total"]}')
    c+=1

num = 0
while True:
    num = int(input('Mostrar os dados de qual jogador?'))
    if num != 999:
        for k in tudo:
            print('-'*5,f'LEVANTAMENTO DO JOGADOR {k["nome"]}','-'*5)
            for j, k in enumerate(tudo[num]['gols']):
                print(f' -> No jogo {j+1} fez {k} gols')
    else:
        print('-'*15)
        print('volte sempre')
        break

