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
from listas.listaOrdenada1k import listaOrdenada1k
from listas.listaOrdenada10k import listaOrdenada10k
from listas.listaOrdenada50k import listaOrdenada50k
from listas.listaOrdenada100k import listaOrdenada100k

#Instaciando graficos e timeit
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
list1kOrdenada = listaOrdenada1k()
list10kOrdenada = listaOrdenada10k()
list50kOrdenada = listaOrdenada50k()
list100kOrdenada = listaOrdenada100k()

#Instanciando Graficos
grafico = geraGrafico()

#Salvando cada tipo de lista em cada variável
#lista = list1k.lista1k()
#lista = list10k.lista10k()
#lista = list50k.lista50k()
#lista = list100k.lista100k()
#lista = list1kOrdenada.listaOrdenada1k()
lista = list10kOrdenada.listaOrdenada10k()
#lista = list50kOrdenada.listaOrdenada50k()
#lista = list100kOrdenada.listaOrdenada100k()

#print(lista)

ultimaPos = len(lista) - 1

#Variáveis com as listas ordenadas e contadores de trocas e comparações
listaOrdenadaBubble, contComparacaoBubble, contTrocaBubble = bubbleSort.bubbleSort(lista.copy())
listaOrdenadaHeap, contComparacaoHeap, contTrocaHeap = heapSort.heapSort(lista.copy())
listaOrdenadaInsertion, contComparacaoInsertion, contTrocaInsertion = insertionSort.insertionSort(lista.copy())
listaOrdenadaMerge, contComparacaoMerge, contTrocaMerge = mergeSort.mergeSort(lista.copy())
listaOrdenadaQuick, contComparacaoQuick, contTrocaQuick = quickSort.quickSort(lista.copy(), 0, ultimaPos)
listaOrdenadaRadix, contComparacaoRadix, contTrocaRadix = radixSort.radixSort(lista.copy())
listaOrdenadaSelection, contComparacaoSelection, contTrocaSelection = selectionSort.selectionSort(lista.copy())
listaOrdenadaShell, contComparacaoShell, contTrocaShell = shellSort.shellSort(lista.copy())

"""
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
tempoExecucaoBubble = timeit.timeit(lambda: bubbleSort.bubbleSort(lista.copy()), number=3)
tempoExecucaoHeap = timeit.timeit(lambda: heapSort.heapSort(lista.copy()), number=3)
tempoExecucaoInsertion = timeit.timeit(lambda: insertionSort.insertionSort(lista.copy()), number=3)
tempoExecucaoMerge = timeit.timeit(lambda: mergeSort.mergeSort(lista.copy()), number=3)
tempoExecucaoQuick = timeit.timeit(lambda: quickSort.quickSort(lista.copy(), 0, ultimaPos), number=3)
tempoExecucaoRadix = timeit.timeit(lambda: radixSort.radixSort(lista.copy()), number=3)
tempoExecucaoSelection = timeit.timeit(lambda: selectionSort.selectionSort(lista.copy()), number=3)
tempoExecucaoShell = timeit.timeit(lambda: shellSort.shellSort(lista.copy()), number=3)

#Exibindo tempo de execução
print ("")
print ("Tempo bubble:", tempoExecucaoBubble, "segundos")
print ("Tempo heap:", tempoExecucaoHeap, "segundos")
print ("Tempo insertion:", tempoExecucaoInsertion, "segundos")
print ("Tempo merge:", tempoExecucaoMerge, "segundos")
print ("Tempo quick:", tempoExecucaoQuick, "segundos")
print ("Tempo radix:", tempoExecucaoRadix, "segundos")
print ("Tempo selection:", tempoExecucaoSelection, "segundos")
print ("Tempo shell:", tempoExecucaoShell, "segundos")
print ("")

#Exibindo contagem de comparações
print ("Comparações bubble:", contComparacaoBubble, "comparações")
print ("Comparações heap:", contComparacaoHeap, "comparações")
print ("Comparações insertion:", contComparacaoInsertion, "comparações")
print ("Comparações merge:", contComparacaoMerge, "comparações")
print ("Comparações quick:", contComparacaoQuick, "comparações")
print ("Comparações radix:", contComparacaoRadix, "comparações")
print ("Comparações selection:", contComparacaoSelection, "comparações")
print ("Comparações shell:", contComparacaoShell, "comparações")
print ("")

#Exibindo contagem de trocas
print ("Trocas bubble:", contTrocaBubble, "trocas")
print ("Trocas heap:", contTrocaHeap, "trocas")
print ("Trocas insertion:", contTrocaInsertion, "trocas")
print ("Trocas merge:", contTrocaMerge, "trocas")
print ("Trocas quick:", contTrocaQuick, "trocas")
print ("Trocas radix:", contTrocaRadix, "trocas")
print ("Trocas selection:", contTrocaSelection, "trocas")
print ("Trocas shell:", contTrocaShell, "trocas")

# Lista com as medias de comparações
listaContagemComparacao = [
    contComparacaoBubble,
    contComparacaoHeap,
    contComparacaoInsertion,
    contComparacaoMerge,
    contComparacaoQuick,
    contComparacaoRadix,
    contComparacaoSelection,
    contComparacaoShell
]

# Lista com as medias de trocas
listaContagemTroca = [
    contTrocaBubble,
    contTrocaHeap,
    contTrocaInsertion,
    contTrocaMerge,
    contTrocaQuick,
    contTrocaRadix,
    contTrocaSelection,
    contTrocaShell
]

# Lista com as medias de execução
listaTempoExecucao = [
    tempoExecucaoBubble     / 3,
    tempoExecucaoHeap       / 3,
    tempoExecucaoInsertion  / 3,
    tempoExecucaoMerge      / 3,
    tempoExecucaoQuick      / 3,
    tempoExecucaoRadix      / 3,
    tempoExecucaoSelection  / 3,
    tempoExecucaoShell      / 3
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
grafico.geraGraficoTempExec(descricaoAlgoritmos, listaTempoExecucao)

# Chamando a função pra exibir o grafico e passando as listas com a contagem de comparações e a descrição dos metodos
grafico.geraGraficoComparacoes(descricaoAlgoritmos, listaContagemComparacao)

# Chamando a função pra exibir o grafico e passando as listas com a contagem de trocas e a descrição dos metodos
grafico.geraGraficoTrocas(descricaoAlgoritmos, listaContagemTroca)