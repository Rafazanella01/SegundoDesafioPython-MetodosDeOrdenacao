class Ordenacao:
    def quickSort(self, lista, primeiraPosicao, ultimaPosicao):

        #pivo = lista[primeiraPosicao]
        #pivo = lista[ultimaPosicao]

        #Aqui é usado o metodo de escolha do pivô mediano de 3 ele é mais rápido do que escolher o primeiro ou o ultimo elemento da lista

        meio = (primeiraPosicao + ultimaPosicao) // 2
        pivo = sorted([lista[primeiraPosicao], lista[meio], lista[ultimaPosicao]])[1]

        ponteiroEsquerda = primeiraPosicao
        ponteiroDireita = ultimaPosicao

        while ponteiroEsquerda <= ponteiroDireita:
            
            while lista[ponteiroEsquerda] < pivo:
                ponteiroEsquerda += 1

            while lista[ponteiroDireita] > pivo:
                ponteiroDireita -= 1

            if ponteiroEsquerda <= ponteiroDireita:
                lista[ponteiroEsquerda], lista[ponteiroDireita] = lista[ponteiroDireita], lista[ponteiroEsquerda]
                ponteiroEsquerda += 1
                ponteiroDireita -= 1

        if primeiraPosicao < ponteiroDireita:
            self.quickSort(lista, primeiraPosicao, ponteiroDireita)
        if ponteiroEsquerda < ultimaPosicao:
            self.quickSort(lista, ponteiroEsquerda, ultimaPosicao)
    
        return lista
