"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF969 - Algoritmos e estrutura de dados
Autor: Hugo Issao Uraga (hiu)
Email: hiu@cin.ufpe.br
Data: 2018-06-03
Copyright(c) 2018 Hugo Issao Uraga
"""
def conjunto(vetor_conjunto):
    '''
    A função retorna o conjunto com todas as posições que deverão ser preenchidas pelo conjunto potência(conjunto das partes)
    '''
    tamanho = len(vetor_conjunto)
    q_pos = 2 ** tamanho

    sub_conjuntos =[]
    for posicoes in range(q_pos):
        sub_conjuntos.append(set())
    return sub_conjuntos

def conjunto_Partes(vetor,sub_conjuntos):
    tamanho = len(vetor)
    for indice in range(tamanho):
        elemento_adiciona = vetor[indice]
        for posicao in range(2  ** tamanho):
            print(posicao)
            operacao = ((posicao // (2 **  indice))  % 2)
            print(operacao)
            if operacao == 0:
                sub_conjuntos[posicao].add(elemento_adiciona)
                print(sub_conjuntos)
lista = [1,2,3,4]
sub_conjuntos = conjunto(lista)
conjunto_Partes(lista,sub_conjuntos)
