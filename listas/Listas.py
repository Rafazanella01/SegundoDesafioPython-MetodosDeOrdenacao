import random

class Listas:

    def lista1k(self):
        lista1k = []
        for _ in range(999):
            novo = random.randint(-100,999)
            lista1k.append(novo)
        return lista1k
         
    def lista10k(self):
        lista10k = []
        for _ in range(9999):
            novo = random.randint(-100,999)
            lista10k.append(novo)
        return lista10k
    
    def lista50k(self):
        lista50k = []
        for _ in range(49999):
            novo = random.randint(-100,999)
            lista50k.append(novo)
        return lista50k
    
    def lista100k(self):
        lista100k = []
        for _ in range(99999):
            novo = random.randint(-99999,99999)
            lista100k.append(novo)
        return lista100k

    #Listas já ordenadas

    def listaOrdenada1k(self):
        listaOrdenada1k = []
        for i in range (999):
            listaOrdenada1k.append(i)
        return listaOrdenada1k
    
    def listaOrdenada10k(self):
        listaOrdenada10k = []
        for i in range (9999):
            listaOrdenada10k.append(i)
        return listaOrdenada10k
    
    def listaOrdenada50k(self):
        listaOrdenada50k = []
        for i in range (9999):
            listaOrdenada50k.append(i)
        return listaOrdenada50k
    
    def listaOrdenada100k(self):
        listaOrdenada100k = []
        for i in range (99999):
            listaOrdenada100k.append(i)
        return listaOrdenada100k
    
    #Demais casos de testes

    def listaVazia(self):
        return []

    def listaRepetida(self):
        repetido = random.randint(-100, 999)
        return [repetido] * 999

    def listaDecrescente(self):
        return list(range(999, -101, -1))
    
    def listaUnicoItem(self):
        lista = [1]
        return lista