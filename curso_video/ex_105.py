#Faça um programa que tenha uma função notas() que pode receber varias notas de alunos e vai retornar um dicionário
#com as seguintes informações:
# quantidades de notas
# a maior nota
# a menor nota
# a media da turma
# a situação (opcional)
# adicione tambem as docstrings na sua função

def notas(*n, situaçao = False):
    """
    -> Retorna informações da avaliação do aluno
    :param n: notas das avaliações
    :param situaçao: Situação final do aluno
    :return: dicionário com as informações gerais do aluno
    """
    lista = n
    soma = 0
    dic = {}
    dic['total'] = len(lista)
    dic['maior'] = max(lista)
    dic['menor'] = min(lista)
    for c in range(len(lista)):
        soma += lista[c]
        m = soma/len(lista)
        dic['media'] = m
    if situaçao == True:
        if m >= 7:
            dic['situação'] = 'APROVADO'
        elif 5 <= m < 7:
            dic['situação'] = 'RAZOÁVEL'
        else:
            dic['situação'] = 'REPROVADO'
    return dic



resp = notas(1,2,3.5,10,6.5, situaçao=True)
print(resp)