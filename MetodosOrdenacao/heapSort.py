class HeapSort:
    def heapSort(self, arr):
        n = len(arr)
        contComparacoes = 0
        contTrocas = 0

        # Build max heap
        for i in range(n // 2, -1, -1):
            comp, trocas = self.heapify(arr, n, i)
            contComparacoes += comp
            contTrocas += trocas

        for i in range(n - 1, 0, -1):
            # Swap
            arr[i], arr[0] = arr[0], arr[i]

            # Heapify root element
            comp, trocas = self.heapify(arr, i, 0)
            contComparacoes += comp
            contTrocas += trocas

        return arr, contComparacoes, contTrocas

    def heapify(self, arr, n, i):
        contComparacoes = 0
        contTrocas = 0

        # Find largest among root and children
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n:
            contComparacoes += 1
            if arr[i] < arr[l]:
                largest = l

        if r < n:
            contComparacoes += 1
            if arr[largest] < arr[r]:
                largest = r

        # If root is not largest, swap with largest and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            contTrocas += 1
            contComparacoes += 1
            comp, trocas = self.heapify(arr, n, largest)
            contComparacoes += comp
            contTrocas += trocas

        return contComparacoes, contTrocas