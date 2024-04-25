from MetodosOrdenacao.quickSort import quickSort
from MetodosOrdenacao.bubbleSort import bubbleSort
import timeit

quickSort = quickSort()
bubbleSort = bubbleSort()

lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]
lista2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]

ultimaPos = len(lista) - 1

listaOrdenadaQuick = quickSort.quickSort(lista, 0, ultimaPos)

listaOrdenadaBubble = bubbleSort.bubbleSort(lista2)

print(listaOrdenadaQuick)
print(listaOrdenadaBubble)