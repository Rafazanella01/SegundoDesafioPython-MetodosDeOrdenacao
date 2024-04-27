class selectionSort:
    def selectionSort(self, vetor):
        tamanho = len(vetor)
        i = 0
        while(i < (tamanho - 1)):          #Utiliza While no lugar do for
            min = i
            for j in range(i+1, tamanho):    #Mantem o o outro for
                if vetor[min] > vetor[j]:      #Compara pra achar um valor menor
                    min = j

            if min != i:                     #Vê se há outro valor menor na lista
                vetor[i], vetor[min] = vetor[min], vetor[i]
            i +=1

        return vetor
