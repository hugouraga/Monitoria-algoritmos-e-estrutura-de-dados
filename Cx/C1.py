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
def conquista(primeira,segunda):
  final = ListaEncadeada()
  i = 0
  j = 0

  while i < len(primeira) or j < len(segunda):
    if i == len(primeira):
      for elem in range(j, len(segunda)):
        final.append(segunda[j])
        j += 1
    elif j == len(segunda):
      for elem in range(i, len(primeira)):
        final.append(primeira[i])
        i += 1
        
    elif primeira[i] <= segunda[j]:
      final.append(primeira[i])
      i += 1

    elif primeira[i] > segunda[j]:
      final.append(segunda[j])
      j += 1

  return final
