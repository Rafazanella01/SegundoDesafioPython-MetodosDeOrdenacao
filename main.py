from MetodosOrdenacao.bubbleSort import bubbleSort
#from MetodosOrdenacao.heapSort import heapSort
#from MetodosOrdenacao.insertionSort import insertionSort
from MetodosOrdenacao.mergeSort import mergeSort
from MetodosOrdenacao.quickSort import quickSort
from MetodosOrdenacao.radixSort import radixSort
from MetodosOrdenacao.selectionSort import selectionSort
from MetodosOrdenacao.shellSort import shellSort
from listas.lista1k import lista1k

import timeit

bubbleSort = bubbleSort()
#heapSort = heapSort()
#insertionSort = insertionSort()
mergeSort = mergeSort()
quickSort = quickSort()
radixSort = radixSort()
selectionSort = selectionSort()
shellSort = shellSort()
list = lista1k()

lista = list.lista1k()
#lista = [281, 878, 174, 566, 943, 417, 525, 803, 966, 182, 74, 787, 698, 121, 156, 389, 586, 673, 286, 491, 629, 642, 390, 586, 434, 78, 478, 808, 386, 124, 16, 996, 843, 747, 297, 53, 698, 216, 807, 156, 401, 739, 883, 516, 990, 422, 807, 42, 72, 623, 611, 768, 84, 996, 213, 284, 62, 851, 218, 155, 272, 875, 259, 273, 638, 385, 658, 390, 556, 608, 529, 823, 75, 48, 687, 18, 196, 209, 876, 251, 374, 552, 58, 743, 745, 101, 582, 910, 593, 566, 735, 322, 747, 673, 384, 866, 384, 871, 806, 759, 120, 828, 57, 131, 224, 917, 280, 123, 432, 356, 557, 353, 468, 904, 83, 363, 862, 344, 504, 941, 289, 65, 361, 74, 370, 791, 773, 584, 176, 308, 716, 126, 675, 948, 784, 929, 754, 538, 398, 335, 912, 637, 756, 153, 193, 902, 748, 242, 65, 496, 698, 413, 285, 994, 768, 19, 323, 792, 744, 76, 921, 42, 92, 274, 601, 961, 153, 847, 998, 191, 31, 692, 689, 741, 359, 351, 565, 742, 899, 866, 298, 480, 262, 510, 441, 605, 994, 189, 273, 851, 777, 791, 574, 984, 778, 589, 7, 991, 994, 661, 608, 360, 663, 767, 360, 482, 598, 23, 783, 137, 180, 36, 505, 455, 752, 289, 632, 299, 110, 321, 136, 275, 596, 852, 241, 481, 334, 208, 282, 845, 108, 68, 179, 872, 1, 28, 837, 197, 603, 752, 582, 816, 241, 389, 229, 408, 699, 852, 414, 324, 355, 182, 143, 188, 122, 687, 522, 108, 693, 81, 864, 406, 651, 899, 694, 148, 793, 581, 568, 115, 991, 201, 465, 617, 677, 914, 62, 324, 707, 57, 99, 0, 210, 969, 739, 54, 202, 831, 995, 631, 475, 464, 196, 992, 491, 131, 399, 921, 30, 3, 988, 118, 191, 936, 782, 254, 794, 566, 929, 480, 948, 403, 609, 581, 315, 891, 369, 686, 294, 140, 55, 0, 668, 466, 197, 707, 300, 318, 929, 554, 283, 675, 365, 419, 756, 302, 805, 474, 469, 746, 659, 871, 554, 419, 207, 605, 6, 597, 568, 402, 843, 789, 714, 803, 877, 561, 818, 468, 39, 360, 537, 299, 565, 122, 795, 801, 998, 369, 736, 693, 999, 287, 498, 724, 777, 910, 887, 214, 987, 292, 719, 727, 283, 442, 242, 280, 515, 847, 14, 312, 404, 542, 8, 140, 331, 584, 367, 416, 102, 675, 549, 118, 230, 717, 41, 945, 576, 232, 809, 68, 209, 482, 717, 65, 521, 108, 374, 964, 97, 879, 982, 903, 116, 418, 225, 699, 537, 997, 44, 228, 542, 504, 387, 329, 741, 419, 429, 699, 640, 581, 128, 531, 72, 84, 100, 807, 867, 220, 383, 366, 538, 586, 233, 714, 582, 992, 643, 116, 608, 279, 488, 538, 485, 490, 192, 185, 770, 142, 433, 890, 573, 707, 0, 132, 66, 556, 89, 639, 618, 615, 125, 953, 34, 722, 949, 783, 177, 740, 332, 958, 361, 983, 992, 628, 915, 957, 843, 840, 584, 807, 98, 933, 998, 786, 987, 442, 709, 463, 248, 872, 256, 846, 107, 56, 755, 134, 152, 44, 628, 495, 11, 217, 162, 392, 208, 445, 977, 1, 622, 943, 736, 971, 767, 984, 963, 736, 124, 508, 964, 247, 541, 118, 398, 525, 229, 210, 748, 405, 667, 689, 17, 115, 455, 170, 913, 793, 516, 810, 73, 970, 180, 988, 186, 209, 892, 859, 897, 129, 396, 557, 208, 553, 80, 40, 797, 515, 164, 475, 640, 421, 67, 149, 745, 174, 513, 35, 808, 289, 100, 351, 554, 884, 753, 905, 320, 455, 712, 388, 234, 165, 246, 301, 194, 20, 46, 216, 696, 884, 304, 913, 532, 965, 758, 936, 653, 17, 216, 144, 738, 210, 236, 89, 755, 814, 776, 192, 751, 244, 235, 612, 73, 527, 40, 909, 849, 623, 305, 511, 949, 297, 31, 455, 798, 204, 380, 746, 277, 867, 537, 420, 97, 342, 351, 753, 862, 71, 976, 965, 349, 491, 689, 605, 306, 351, 292, 358, 576, 340, 524, 514, 998, 488, 554, 268, 879, 556, 66, 671, 910, 151, 540, 737, 226, 511, 4, 286, 855, 58, 701, 348, 926, 777, 941, 782, 374, 818, 727, 416, 683, 997, 677, 152, 179, 700, 55, 656, 408, 214, 354, 187, 952, 449, 948, 229, 599, 341, 299, 346, 629, 728, 47, 684, 286, 5, 300, 83, 658, 187, 520, 19, 295, 144, 339, 592, 313, 438, 343, 201, 181, 134, 34, 214, 61, 170, 716, 936, 911, 534, 146, 287, 873, 783, 937, 537, 366, 199, 379, 294, 788, 757, 324, 102, 257, 406, 253, 49, 231, 766, 653, 647, 403, 371, 812, 405, 168, 751, 648, 814, 348, 55, 916, 177, 382, 167, 597, 325, 193, 135, 635, 479, 610, 113, 902, 519, 305, 294, 101, 205, 543, 281, 471, 315, 691, 585, 273, 550, 504, 735, 795, 859, 769, 298, 342, 284, 507, 486, 788, 563, 627, 9, 473, 723, 212, 814, 666, 486, 987, 587, 269, 690, 347, 32, 651, 821, 43, 604, 91, 220, 361, 278, 469, 593, 443, 11, 653, 407, 649, 133, 496, 792, 849, 298, 175, 266, 916, 188, 680, 615, 752, 316, 823, 215, 607, 961, 858, 377, 865, 203, 461, 273, 719, 182, 11, 760, 981, 477, 914, 182, 557, 667, 45, 54, 693, 91, 184, 974, 591, 854, 976, 623, 442, 697, 657, 371, 768, 216, 554, 244, 550, 668, 24, 253, 886, 406, 473, 806, 696, 742, 497, 596, 305, 853, 196, 968, 308, 437, 202, 960, 916, 628, 891, 328, 615, 677, 298, 702, 161, 556, 722, 133, 660, 477, 996, 13, 491, 98, 590, 151, 395, 110, 509, 920, 201, 692, 397, 90, 70, 62, 299, 320, 816, 999, 387, 316, 502, 21, 627, 819, 459, 959, 898, 574, 665, 875, 785, 837, 394, 816, 766, 173, 200, 230, 977, 258, 881, 127, 419, 401, 734, 89, 130, 175, 588, 989, 972, 56, 441, 321, 381, 96, 337, 60, 389, 478, 166, 860, 610, 851, 394]


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