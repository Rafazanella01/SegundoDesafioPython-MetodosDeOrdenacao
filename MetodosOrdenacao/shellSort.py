class shellSort:
    def shellSort(self, Lista):
        n = len(Lista)

        #intervalo utilizando metodo de dividir pela metade melhor em listas curtas
        intervalo = n//2
        contComparacoes = 0
        contTrocas = 0

        trocas = 0
        while intervalo > 0:
            for i in range(intervalo, n): #pega o intervalo e verifica até o tamanho da tabela
                valorAtual = Lista[i]
                indexAux = i
                # Desloca os elementos anteriores intervalo-posicionados até a posição correta para Lista[i]
                while indexAux >= intervalo and Lista[indexAux - intervalo] > valorAtual: #verifica se os valores de determinado setor são menores que sua outra versão
                    Lista[indexAux] = Lista[indexAux - intervalo] #troca o valor maior do começo do  número para outro com mesmo numero
                    indexAux -= intervalo #diminui para poder trocar o valor menor para frente
                    contComparacoes += 1
                    contTrocas += 1
                Lista[indexAux] = valorAtual #se tiver trocado, o valor menor vem para frente, se nao fica igual
            intervalo //= 2
        return Lista, contComparacoes, contTrocas