class insertionSort:
    def insertionSort(self, lista):
        contComparacoes = 0
        contTrocas = 0

        n = len(lista)
        for i in range(1, n):
            chave = lista[i]
            j = i - 1
            while j >= 0 and lista[j] > chave:
                contComparacoes += 1
                lista[j + 1] = lista[j]
                j -= 1
                contTrocas += 1
            # Conta a comparação que quebra o laço while
            if j >= 0:
                contComparacoes += 1
            lista[j + 1] = chave

        return lista, contComparacoes, contTrocas
