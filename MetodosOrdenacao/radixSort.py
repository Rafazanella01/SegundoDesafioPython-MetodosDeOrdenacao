class radixSort:
    def counting_sort(self, array, exp):
        n = len(array)    # Obtendo o tamanho da lista
        output = [0] * n    # Inicializando uma lista de saída com o mesmo tamanho da lista de entrada
        count = [0] * 10    # Inicializando uma lista de contagem para cada dígito de 0 a 9


        for i in range(n):  # Contando a ocorrência de cada dígito na posição 'exp' e armazenando na lista de contagem
            index = array[i] // exp  # Determinando o índice com base no dígito na posição 'exp'
            count[index % 10] += 1


        for i in range(1, 10):  # Atualizando a lista de contagem para conter as posições corretas dos elementos
            count[i] += count[i - 1]

        i = n - 1   # Construindo a lista de saída usando as posições corretas dos elementos
        while i >= 0:
            index = array[i] // exp  # Determinando o índice com base no dígito na posição 'exp'
            output[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(n):  # Copiando os elementos ordenados de volta para a lista original
            array[i] = output[i]

    def radixSort(self, lista):
        max_num = max(lista)  # Encontrando o maior número na lista pela função max()
        exp = 1
        while max_num // exp > 0:   # Iterando até que o dígito mais significativo do maior número seja processado
            self.counting_sort(lista, exp) # Chamando o counting_sort para ordenar os elementos com base no dígito na posição 'exp'
            exp *= 10
        return lista