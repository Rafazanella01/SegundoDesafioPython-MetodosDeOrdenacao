from MetodosOrdenacao.bubbleSort import bubbleSort
from MetodosOrdenacao.heapSort import heapSort
from MetodosOrdenacao.insertionSort import insertionSort
from MetodosOrdenacao.mergeSort import mergeSort
from MetodosOrdenacao.quickSort import quickSort
from MetodosOrdenacao.radixSort import radixSort
from MetodosOrdenacao.selectionSort import selectionSort
from MetodosOrdenacao.shellSort import shellSort
from listas.lista1k import lista1k
from listas.lista50k import lista50k
from geraGrafico import geraGrafico
import timeit

bubbleSort = bubbleSort()
heapSort = heapSort()
insertionSort = insertionSort()
mergeSort = mergeSort()
quickSort = quickSort()
radixSort = radixSort()
selectionSort = selectionSort()
shellSort = shellSort()
list1k = lista1k()
list50k = lista50k()
grafico = geraGrafico()

#lista = list1k.lista1k()
lista = list50k.lista50k()

ultimaPos = len(lista) - 1

#listaOrdenadaBubble = bubbleSort.bubbleSort(lista)

#listaOrdenadaHeap = heapSort.heapSort(lista)

#listaOrdenadaInsertion = insertionSort.insertionSort(lista)

#listaOrdenadaMerge = mergeSort.mergeSort(lista)

#listaOrdenadaQuick = quickSort.quickSort(lista, 0, ultimaPos)

#listaOrdenadaRadix = radixSort.radixSort(lista)

#listaOrdenadaSelection = selectionSort.selectionSort(lista)

#listaOrdenadaShell = shellSort.shellSort(lista)

#print("BubbleSort: ", listaOrdenadaBubble)
#print("HeapSort: ", listaOrdenadaHeap)
#print("InsertionSort: ", listaOrdenadaInsertion)
#print("MergeSort: ", listaOrdenadaMerge)
#print("QuickSort: ", listaOrdenadaQuick)
#print("RadixSort: ", listaOrdenadaRadix)
#print("SelectionSort: ", listaOrdenadaSelection)
#print("ShellSort: ", listaOrdenadaShell)

tempoExecucaoBubble = timeit.timeit(lambda: bubbleSort.bubbleSort(lista), number=10000)

tempoExecucaoHeap = timeit.timeit(lambda: heapSort.heapSort(lista), number=10000)

tempoExecucaoInsertion = timeit.timeit(lambda: insertionSort.insertionSort(lista), number=10000)

tempoExecucaoMerge = timeit.timeit(lambda: mergeSort.mergeSort(lista), number=10000)

tempoExecucaoQuick = timeit.timeit(lambda: quickSort.quickSort(lista, 0, ultimaPos), number=10000)

tempoExecucaoRadix = timeit.timeit(lambda: radixSort.radixSort(lista), number=10000)

tempoExecucaoSelection = timeit.timeit(lambda: selectionSort.selectionSort(lista), number=10000)

tempoExecucaoShell = timeit.timeit(lambda: shellSort.shellSort(lista), number=10000)


print ("Tempo bubble:", tempoExecucaoBubble, "segundos")

print ("Tempo heap:", tempoExecucaoHeap, "segundos")

print ("Tempo insertion:", tempoExecucaoInsertion, "segundos")

print ("Tempo merge:", tempoExecucaoMerge, "segundos")

print ("Tempo quick:", tempoExecucaoQuick, "segundos")

print ("Tempo radix:", tempoExecucaoRadix, "segundos")

print ("Tempo selection:", tempoExecucaoSelection, "segundos")

print ("Tempo shell:", tempoExecucaoShell, "segundos")

# Lista com os tempos de execução
listaTempoExecucao = [
    tempoExecucaoBubble,
    tempoExecucaoHeap,
    tempoExecucaoInsertion,
    tempoExecucaoMerge,
    tempoExecucaoQuick,
    tempoExecucaoRadix,
    tempoExecucaoSelection,
    tempoExecucaoShell
]

# Nomes dos algoritmos de ordenação
descricaoAlgoritmos = [
    "BubbleSort",
    "HeapSort",
    "InsertionSort",
    "MergeSort",
    "QuickSort",
    "RadixSort",
    "SelectionSort",
    "ShellSort"
]

grafico.geraGrafico(descricaoAlgoritmos, listaTempoExecucao)