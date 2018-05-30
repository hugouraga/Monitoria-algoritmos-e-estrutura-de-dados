def produtoMatrizes(matriz1, matrizTransposta):
    matrizResultante = []
    aux = []
    res = 0
    contador = 0
    apontador = 0
    for lista in matriz1:
        while apontador < len(matrizTransposta[0]):
            for elementos in matrizTransposta:
                res += lista[contador] * matrizTransposta[contador][apontador]
                contador += 1
            aux.append(res)
            apontador += 1
            res = 0
            contador = 0
        matrizResultante.append(aux)
        aux = []
        apontador = 0
    return matrizResultante
def transposta(matriz2):
    matrizTransposta = []
    contador = 0
    aux = []
    while contador < len(matriz2[0]):
        for elementos in matriz2:
            aux.append(elementos[contador])
        contador += 1
        matrizTransposta.append(aux)
        aux = []
    return matrizTransposta


def verificaMatriz(matriz1,matriz2):
    n_coluna = len(matriz1[0])
    n_linhas = len(matriz2[0])

    if n_coluna == n_linhas:
        print("realizando o produto entre as matrizes...")
        return True
    else:
        print("não é possível realizar a operação")
        return False

def convertendoString(matriz):
    verificacao = ""
    vetor = []
    vetorAux = []
    for elementos in matriz:
        verificacao += elementos
        if elementos == "]" and verificacao != "]":
            vetor.append(vetorAux)
            vetorAux = []
            verificacao = ""
        elif elementos != "[" and elementos != "]" and elementos != ",":
            vetorAux.append(int(elementos))

    return vetor

matriz1 = input("Forneça a primeira matriz -> ")
matriz1 = convertendoString(matriz1)

matriz2 = input("Forneça a segunda matriz -> ")
matriz2 = convertendoString(matriz2)

teste = verificaMatriz(matriz1,matriz2)

if teste:
    matrizTransposta =  transposta(matriz2)
    print(produtoMatrizes(matriz1,matrizTransposta))
