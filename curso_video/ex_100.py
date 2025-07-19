#faça um programa que tenha uma lista chamada numeros e duas funções chamadas sorteio() e somapar(). A primeira função
#vai sortear 5 numeros e vai coloca-los dentro da lista e a segunda função vai mostrar a soma entre todos os vetores
#pares sorteados pela função anterior

from random import randint

num = []

def sorteio(a):
    for r in range(0,5):
        
