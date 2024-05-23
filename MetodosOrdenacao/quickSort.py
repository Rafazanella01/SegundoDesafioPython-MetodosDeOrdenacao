class QuickSort:
    def quickSort(self, lista, primeiraPosicao, ultimaPosicao):
        meio = (primeiraPosicao + ultimaPosicao) // 2
        pivo = sorted([lista[primeiraPosicao], lista[meio], lista[ultimaPosicao]])[1]

        contComparacoes = 0
        contTrocas = 0

        ponteiroEsquerda = primeiraPosicao
        ponteiroDireita = ultimaPosicao

        while ponteiroEsquerda <= ponteiroDireita:
            while lista[ponteiroEsquerda] < pivo:
                ponteiroEsquerda += 1
                contComparacoes += 1

            while lista[ponteiroDireita] > pivo:
                ponteiroDireita -= 1
                contComparacoes += 1

            if ponteiroEsquerda <= ponteiroDireita:
                lista[ponteiroEsquerda], lista[ponteiroDireita] = lista[ponteiroDireita], lista[ponteiroEsquerda]
                ponteiroEsquerda += 1
                ponteiroDireita -= 1
                contTrocas += 1

        if primeiraPosicao < ponteiroDireita:
            lista, comp1, trocas1 = self.quickSort(lista, primeiraPosicao, ponteiroDireita)
            contComparacoes += comp1
            contTrocas += trocas1

        if ponteiroEsquerda < ultimaPosicao:
            lista, comp2, trocas2 = self.quickSort(lista, ponteiroEsquerda, ultimaPosicao)
            contComparacoes += comp2
            contTrocas += trocas2
    
        return lista, contComparacoes, contTrocas