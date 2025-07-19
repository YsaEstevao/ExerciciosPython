#faça um mini sistema que utilize o interactive help do python. O usuario vai digitar o comendo e o manual vai aparecer
#Quando o usuário digitar a palavra "fim", o programa se encerrará
#obs: use cores

def escreva(a):
    tm = (len(a)//2)*2
    print('-'*(len(a)+(tm+2)))
    print(' '*(len(a)//2),a)
    print('-' * (len(a) + (tm + 2)))

e = 0

while True:
    escreva('\033[0;30;42mSistema de Ajuda PyHelp\033[m')
    e = input('Função ou Biblioteca > ')
    if e == "fim":
        escreva('Até logo')
        break
    else:
        escreva(f"Acessando o manual do comando '{e}'")
        help(e)

