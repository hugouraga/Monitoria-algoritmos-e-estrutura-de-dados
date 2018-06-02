
def funcDOIS(lista,num):
    if num == 0 or num == 1:
        return num
    else:
        if lista[num-1] == None:
            lista[num-1] = funcDOIS(lista,num-1)
        if lista[num-2] == None:
            lista[num-2] = funcDOIS(lista,num-2)

    return lista[num-1] + lista[num-2]
lista = [
    1,10,6]
num = len(lista)
print(funcDOIS(lista,num))

"""
A função retorna a soma de dois elementos da lista(caso existam valores na lista), tais que a soma é realizada com um elemento e seu anterior caso
ambos sejam diferentes de None. Caso a lista seja formada só por elementos None, a função retorna a sequência fibonacci no vetor inserido.
O código é uma otimização pois ele realiza a soma de dois elementos da lista(o atual e seu anterior) utilizando recursão e onde no melhor caso
 não necessita percorrer toda a lista.
"""


