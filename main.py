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
lista = list1k.lista1k()
#lista = list10k.lista10k()
#lista = list50k.lista50k()
#lista = list100k.lista100k()

#print(lista)

ultimaPos = len(lista) - 1

"""
#Variáveis com as listas ordenadas e contadores de trocas e comparações
listaOrdenadaBubble, contComparacaoBubble, contTrocaBubble = bubbleSort.bubbleSort(lista)
listaOrdenadaHeap, contComparacaoHeap, contTrocaHeap = heapSort.heapSort(lista)
listaOrdenadaInsertion, contComparacaoInsertion, contTrocaInsertion = insertionSort.insertionSort(lista)
listaOrdenadaMerge, contComparacaoMerge, contTrocaMerge = mergeSort.mergeSort(lista)
listaOrdenadaQuick, contComparacaoQuick, contTrocaQuick = quickSort.quickSort(lista, 0, ultimaPos)
listaOrdenadaRadix, contComparacaoRadix, contTrocaRadix = radixSort.radixSort(lista)
listaOrdenadaSelection, contComparacaoSelection, contTrocaSelection = selectionSort.selectionSort(lista)
listaOrdenadaShell, contComparacaoShell, contTrocaShell = shellSort.shellSort(lista)

#Exibindo as listas ordenadas

#BubbleSort
print("BubbleSort: ", listaOrdenadaBubble)
print("Contador de comparações BubbleSort: ", contComparacaoBubble)
print("Contador de trocas BubbleSort: ", contTrocaBubble)

#HeapSort
print("HeapSort: ", listaOrdenadaHeap)
print("Contador de comparações HeapSort: ", contComparacaoHeap)
print("Contador de trocas HeapSort: ", contTrocaHeap)

#InsertionSort
print("InsertionSort: ", listaOrdenadaInsertion)
print("Contador de comparações InsertionSort: ", contComparacaoInsertion)
print("Contador de trocas InsertionSort: ", contTrocaInsertion)

#MergeSort
print("MergeSort: ", listaOrdenadaMerge)
print("Contador de comparações MergeSort: ", contComparacaoMerge)
print("Contador de trocas MergeSort: ", contTrocaMerge)

#QuickSort
print("QuickSort: ", listaOrdenadaQuick)
print("Contador de comparações QuickSort: ", contComparacaoQuick)
print("Contador de trocas QuickSort: ", contTrocaQuick)

#RadixSort
print("RadixSort: ", listaOrdenadaRadix)
print("Contador de comparações RadixSort: ", contComparacaoRadix)
print("Contador de trocas RadixSort: ", contTrocaRadix)

#SelectionSort
print("SelectionSort: ", listaOrdenadaSelection)
print("Contador de comparações SelectionSort: ", contComparacaoSelection)
print("Contador de trocas SelectionSort: ", contTrocaSelection)

#ShellSort
print("ShellSort: ", listaOrdenadaShell)
print("Contador de comparações ShellSort: ", contComparacaoShell)
print("Contador de trocas ShellSort: ", contTrocaShell)
"""

#Tempo de execução de cada metodo
tempoExecucaoBubble = timeit.timeit(lambda: bubbleSort.bubbleSort(lista), number=10)
tempoExecucaoHeap = timeit.timeit(lambda: heapSort.heapSort(lista), number=10)
tempoExecucaoInsertion = timeit.timeit(lambda: insertionSort.insertionSort(lista), number=10)
tempoExecucaoMerge = timeit.timeit(lambda: mergeSort.mergeSort(lista), number=10)
tempoExecucaoQuick = timeit.timeit(lambda: quickSort.quickSort(lista, 0, ultimaPos), number=10)
tempoExecucaoRadix = timeit.timeit(lambda: radixSort.radixSort(lista), number=10)
tempoExecucaoSelection = timeit.timeit(lambda: selectionSort.selectionSort(lista), number=10)
tempoExecucaoShell = timeit.timeit(lambda: shellSort.shellSort(lista), number=10)

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

#Chamando a função pra exibir o grafico e passando as listas com o tempo de execução e a descrição dos metodos
grafico.geraGrafico(descricaoAlgoritmos, listaTempoExecucao)