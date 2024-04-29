class bubbleSort:   
    def bubbleSort(self, vetor):
        contTroca=0
        n = len(vetor)
        troca = True
        while troca:
            troca = False
            for i in range(n-1):
                if vetor[i] > vetor[i+1]:
                    vetor[i], vetor[i+1] = vetor[i+1], vetor[i]
                    troca = True
                    contTroca += 1
            n -= 1
        return vetor, contTroca