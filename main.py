from MetodosOrdenacao.quickSort import quickSort
import timeit

 = quickSort()

lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]

ultimaPos = len(lista) - 1

listaOrdenada = ordenacao.quickSort(lista, 0, ultimaPos)

tempoExecucao = timeit.timeit(lambda: ordenacao.quickSort(lista, 0, ultimaPos), number=10000)

print(f"Tempo de execução: {round(tempoExecucao, 5)} segundos")

print(listaOrdenada)