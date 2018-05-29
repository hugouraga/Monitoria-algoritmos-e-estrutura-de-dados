# Monitoria-algoritmos-e-estrutura-de-dados

A1 - ​Analise o trecho de código abaixo, explique seu funcionamento e explique por que ele
poderia ser considerado uma otimização.

        def funcDOIS(lista,num):
            if num == 0 or num == 1:
                return num
            else:
                if lista[num-1] == None:
                    lista[num-1] = funcDOIS(lista,num-1)
                if lista[num-2] == None:
                    lista[num-2] = funcDOIS(lista,num-2)

            return lista[num-1] + lista[num-2]

A2 ​- Analise os trechos de código abaixo e explique o seu funcionamento e diferenças:

    def em_ordem (self, p):
        if not p is None:
            self.em_ordem (p.esq)
            print(p.valor)
            self.em_ordem (p.dir)

    def pre_ordem (self, p):
        if not p is None:
            print(p.valor)
            self.pre_ordem (p.esq)
            self.pre_ordem (p.dir)

    def pos_ordem (self, p):
        if not p is None:
            self.pos_ordem (p.esq)
            self.pos_ordem (p.dir)
            print(p.valor)
            
C1 - ​O código a seguir está errado​. Descubra o que o código deveria fazer, quais são os
erros e conserte-o. Altamente recomendado que nessa questão você use o debugger do
Eclipse ou alguma outra IDE com um bom debugger.

    def conquista(primeira,segunda):
      final = ListaEncadeada()
      i = 0
      j = 0
  
      while i < len(primeira) or j < len(segunda):

        if primeira[i] <= segunda[j]:
          final.append(primeira[i])
          i += 1

        else:
          final.append(segunda[j])
          j += 1

        if i == len(primeira):
          for elem in range(j, segunda):
            final.append(segunda[j])

        else:
          for elem in range(j, primeira):
            final.append(primeira[j])

      return final

Você tem alguma observação de como o uso de Lista Encadeada poderia ser
otimizado para essa função?


Q1 - Implemente um programa que recebe duas matrizes e retorna o resultado da
multiplicação da primeira matriz pela transposta da segunda. Obs: Matriz transposta é a
matriz que se obtém da troca de linhas por colunas de uma dada matriz.


Q2 - ​Um problema bastante recorrente em diversos problemas de computação e estatística
é o de determinar raízes ou zeros de uma função. Um dos métodos mais eficientes para
isso é o método de Newton-Raphson. Esse é um método iterativo que, a cada iteração,
encontra uma melhor aproximação para o zero da função
(https://pt.wikipedia.org/wiki/Método_de_Newton-Raphson). A ideia básica é usar a seguinte
fórmula para aproximar valores de x:

onde x_n+1 é o valor de x na (n+1)-ésima iteração, f é a função que se deseja calcular a
raiz, e f' é sua primeira derivada. Por questões numéricas da implementação computacional
de números reais, é comum aceitar como raiz da função um valor próximo a zero (conforme
um parâmetro de tolerância definido pelo usuário).
Implemente o método de Newton-Raphson em Python para funções polinomiais. Seu
programa deve receber como entrada uma lista de coeficientes do polinômio e a tolerância
desejada, e deve imprimir o valor de x e o número de iterações necessárias para
determiná-lo.


Q3 - ​Implemente um algoritmo em Python que receba como entrada um conjunto de valores
e imprima o conjunto potência desse conjunto.
