palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futuro')

for c in range(len(palavras)):
    uma = palavras[c]
    print(f'\npalavra {uma.upper()} tem as vogais: ',end='')
    for j in range(len(uma)):
        if uma[j] == 'a' or uma[j] == 'e' or uma[j] == 'i' or uma[j] == 'o' or uma[j] == 'u':
            print(uma[j], end=' ')