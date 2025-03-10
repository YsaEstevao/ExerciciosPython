n = 0
quantos = 0
soma = 0
while True:
    n = int(input('digite um numero: '))
    if n == 999:
            break
    soma += n
    quantos += 1
print(f'foram digitados {quantos} numeros e sua soma é {soma}')