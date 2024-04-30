#Instanciando os metodos de ordenação
from MetodosOrdenacao.insertionSort import insertionSort
from MetodosOrdenacao.selectionSort import selectionSort
from MetodosOrdenacao.bubbleSort import bubbleSort
from MetodosOrdenacao.mergeSort import mergeSort
from MetodosOrdenacao.quickSort import quickSort
from MetodosOrdenacao.radixSort import radixSort
from MetodosOrdenacao.shellSort import shellSort
from MetodosOrdenacao.heapSort import heapSort

#Instanciando as listas
from listas.lista1k import lista1k
from listas.lista10k import lista10k
from listas.lista50k import lista50k
from listas.lista100k import lista100k

from geraGrafico import geraGrafico
import timeit

#Instanciando os objetos das classes de cada metodo
insertionSort = insertionSort()
selectionSort = selectionSort()
bubbleSort = bubbleSort()
mergeSort = mergeSort()
quickSort = quickSort()
radixSort = radixSort()
shellSort = shellSort()
heapSort = heapSort()

#Instanciando as classes de cada tipo de lista aleatória
list1k = lista1k()
list10k = lista10k()
list50k = lista50k()
list100k = lista100k()

grafico = geraGrafico()

#Salvando cada tipo de lista em cada variável
#lista = list1k.lista1k()
#lista = list10k.lista10k()
lista = list50k.lista50k()
#lista = list100k.lista100k()

ultimaPos = len(lista) - 1

"""
listaOrdenadaBubble, contador = bubbleSort.bubbleSort(lista)
listaOrdenadaHeap = heapSort.heapSort(lista)

listaOrdenadaInsertion = insertionSort.insertionSort(lista)
listaOrdenadaMerge = mergeSort.mergeSort(lista)
listaOrdenadaQuick = quickSort.quickSort(lista, 0, ultimaPos)
listaOrdenadaRadix = radixSort.radixSort(lista)
listaOrdenadaSelection = selectionSort.selectionSort(lista)
listaOrdenadaShell = shellSort.shellSort(lista)

print("BubbleSort: ", listaOrdenadaBubble)
print("Contador BubbleSort: ", contador)

print("HeapSort: ", listaOrdenadaHeap)
print("InsertionSort: ", listaOrdenadaInsertion)
print("MergeSort: ", listaOrdenadaMerge)
print("QuickSort: ", listaOrdenadaQuick)
print("RadixSort: ", listaOrdenadaRadix)
print("SelectionSort: ", listaOrdenadaSelection)
print("ShellSort: ", listaOrdenadaShell)
"""

#Tempo de execução de cada metodo
tempoExecucaoBubble = timeit.timeit(lambda: bubbleSort.bubbleSort(lista), number=1)
tempoExecucaoHeap = timeit.timeit(lambda: heapSort.heapSort(lista), number=1)
tempoExecucaoInsertion = timeit.timeit(lambda: insertionSort.insertionSort(lista), number=1)
tempoExecucaoMerge = timeit.timeit(lambda: mergeSort.mergeSort(lista), number=1)
tempoExecucaoQuick = timeit.timeit(lambda: quickSort.quickSort(lista, 0, ultimaPos), number=1)
tempoExecucaoRadix = timeit.timeit(lambda: radixSort.radixSort(lista), number=1)
tempoExecucaoSelection = timeit.timeit(lambda: selectionSort.selectionSort(lista), number=1)
tempoExecucaoShell = timeit.timeit(lambda: shellSort.shellSort(lista), number=1)

#Exibindo tempo de execução
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