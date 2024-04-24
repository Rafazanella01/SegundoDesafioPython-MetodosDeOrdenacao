def bubbleSort(vetor):
    #def bubbleSorte(vetor):
    n = len(vetor)
    troca = True
    while troca:
        troca = False
        for i in range(n-1):
            if vetor[i] > vetor[i+1]:
                vetor[i], vetor[i+1] = vetor[i+1], vetor[i]
                troca = True
        n -= 1
    return vetor