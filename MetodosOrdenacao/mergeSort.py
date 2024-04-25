class mergeSort:
    def mergesort(self, lista, inicio=0, fim=None):
        if fim is None:
            fim = len(lista)
        if(fim - inicio > 1):
            meio = (fim + inicio)//2
            mergesort(lista, inicio, meio)
            mergesort(lista, meio, fim)
            merge(lista, inicio, meio, fim)

    def merge(self, lista, inicio, meio, fim):
        esquerda = lista[inicio:meio]
        direita = lista[meio:fim]
        e, d = 0, 0
        for k in range(inicio, fim):
            if e >= len(esquerda):
                lista[k] = direita[d]
                d = d + 1
            elif d >= len(direita):
                lista[k] = esquerda[e]
                e = e + 1
            elif esquerda[e] < direita[d]:
                lista[k] = esquerda[e]
                e = e + 1
            else:
                lista[k] = direita[d]
                d = d + 1