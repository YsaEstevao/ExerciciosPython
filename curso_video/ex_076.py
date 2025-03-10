mercado = ('Agua',1.50,'Pao',0.80,'Cachorro',3.50,'Gato',1.00,'JANELA',100,'Professor',300,'Jesus', 0.00)

print('-'*40)
print(' '*9, 'LISTAGEM DE PREÇOS')
print('-'*40)
for c in range(len(mercado)):
    produtos = mercado[c]
    if c % 2 == 0:
        for i in range(len(produtos)):
            d = i + 1
        print(f'{mercado[c]}{'.'*(30-d)}R$',mercado[c+1])
print('-'*40)



