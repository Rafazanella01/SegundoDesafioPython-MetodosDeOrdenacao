class mergeSort:
    def mergeSort(self, arr):
        # Verifica se a lista possui mais de um elemento
        if len(arr) > 1:

            meio = len(arr) // 2 # Pega o a posição central do array
            esquerda = arr[:meio]  # Separa a metade esquerda da lista
            direita = arr[meio:]   # Separa a metade direita da lista

            # Ordena recursivamente as duas metades
            self.mergeSort(esquerda)
            self.mergeSort(direita)

            # Junta as duas metades ordenadas
            i = j = k = 0
            while i < len(esquerda) and j < len(direita):
                if esquerda[i] < direita[j]:
                    arr[k] = esquerda[i]
                    i += 1
                else:
                    arr[k] = direita[j]
                    j += 1
                k += 1

            # Adiciona quaisquer elementos restantes da metade esquerda
            while i < len(esquerda):
                arr[k] = esquerda[i]
                i += 1
                k += 1

            # Adiciona quaisquer elementos restantes da metade direita
            while j < len(direita):
                arr[k] = direita[j]
                j += 1
                k += 1

        return arr