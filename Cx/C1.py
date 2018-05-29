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
