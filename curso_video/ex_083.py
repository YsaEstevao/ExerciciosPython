ex = list(input('Digite uma expressão: '))

c = 0

for i in range(len(ex)):
    if ex[i] == '(' or ex[i] == ')':
        c += 1
if c == 0:
    print('Expressão invalida!')
elif c % 2 == 0:
    print('Expressão válida :)')
else:
    print('Expressão invalida!')
