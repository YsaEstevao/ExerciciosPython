import time
from arquivos import *



def estilo(p): 
    print('-'*40)
    print(p.center(40))
    print('-'*40)
    print('\033[33m1\033[0m - \033[34mVer pessoas cadastradas\033[0m')
    print('\033[33m2\033[0m - \033[34mCadastrar nova pessoa\033[0m')
    print('\033[33m3\033[0m - \033[34mSair do sistema\033[0m')


arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)




n= None
def cadastro():
    estilo('MENU PRINCIPAL')
    n = input('\033[33mSua opção: \033[0m')
    try:
        n.isnumeric
        n = int(n)
        if n == 1:
            print('-'*40)
            print('PESSOAS CADASTRADAS'.center(40))
            print('-'*40)
            lerArquivo(arq)
            time.sleep(1)
            cadastro()
        if n == 2:
            print('-'*40)
            print('NOVO CADASTRO'.center(40))
            print('-'*40)
            nome = str(input('Nome: '))
            from ex_113Teste import leiaInt
            idade = leiaInt('Idade: ')
            cadastrar(arq,nome,idade)
            time.sleep(1)
            cadastro()
        if n == 3:
            print('-'*40)
            print('Saindo do sistema'.center(40))
            print('-'*40)
        if n == 0 or n > 3:
            if n == 3:
                return
            raise ValueError
    except ValueError:
        time.sleep(0.50)
        print('\033[31mERRO: Por favor digite uma opção válida!\033[0m')
        time.sleep(0.50)
        cadastro()



sistema = cadastro()
