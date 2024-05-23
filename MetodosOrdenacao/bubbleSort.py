class BubbleSort:   
    def bubbleSort(self, vetor):
        contComparacoes = 0
        contTrocas = 0
        n = len(vetor)
        troca = True
        while troca:
            troca = False
            for i in range(n-1):
                contComparacoes += 1
                if vetor[i] > vetor[i+1]:
                    vetor[i], vetor[i+1] = vetor[i+1], vetor[i]
                    troca = True
                    contTrocas += 1
            n -= 1
        return vetor, contComparacoes, contTrocas