# Monitoria-algoritmos-e-estrutura-de-dados

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
