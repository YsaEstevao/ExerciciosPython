times = ('Fortaleza','Botafogo','Palmeiras','Flamengo','São Paulo','Bahia','Cruzeiro','Nova Iguaçu',"Atlético-MG",'Athletico-PR','Internacional','Criciúma','Juventude','Grêmio','Bragantino','Fluminense','EC Vitória','Corinthians','Cuiabá','Atlético-GO')

print(f'os 5 primeiros colocados são: {times[0:5]}'),
print(f'os 4 ultimos colocados são: {times[:15:-1]}')
print(f'Colocando em ordem alfabetica fica:{sorted(times)}')
for c , p in enumerate(times):
    if times[c] == 'Botafogo':
        print(f'O Botafogo está na posição: {(c)+1}')