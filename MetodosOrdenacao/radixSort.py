class radixSort:
    def counting_sort(self, arr, exp, contComparacao, contTroca):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        i = 0
        for i in range(0, len(arr)):
            contComparacao += 1
            if arr[i] != output[i]:
                contTroca += 1
            arr[i] = output[i]

        return arr, contComparacao, contTroca

    def radixSort(self, arr):
        contComparacao = 0
        contTroca = 0
        max_num = max(arr)
        exp = 1
        while max_num // exp > 0:
            arr, contComparacao, contTroca = self.counting_sort(arr, exp, contComparacao, contTroca)
            exp *= 10

        return arr, contComparacao, contTroca