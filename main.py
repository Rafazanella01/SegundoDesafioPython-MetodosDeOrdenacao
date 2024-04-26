from MetodosOrdenacao.bubbleSort import bubbleSort
#from MetodosOrdenacao.heapSort import heapSort
#from MetodosOrdenacao.insertionSort import insertionSort
from MetodosOrdenacao.mergeSort import mergeSort
from MetodosOrdenacao.quickSort import quickSort
from MetodosOrdenacao.radixSort import radixSort
from MetodosOrdenacao.selectionSort import selectionSort
from MetodosOrdenacao.shellSort import shellSort

import timeit

bubbleSort = bubbleSort()
#heapSort = heapSort()
#insertionSort = insertionSort()
mergeSort = mergeSort()
quickSort = quickSort()
radixSort = radixSort()
selectionSort = selectionSort
shellSort = shellSort()


lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]

ultimaPos = len(lista) - 1
listaOrdenadaBubble = bubbleSort.bubbleSort(lista)

#listaOrdenadaHeap = heapSort.heapSort(lista)

#listaOrdenadaInsertion = insertionSort.insertionSort(lista)

listaOrdenadaMerge = mergeSort.mergeSort(lista)

listaOrdenadaQuick = quickSort.quickSort(lista, 0, ultimaPos)

listaOrdenadaRadix = radixSort.radixSort(lista)

listaOrdenadaSelection = selectionSort.selectionSort(lista)

listaOrdenadaShell = shellSort.shellSort(lista)




print(listaOrdenadaSelection)