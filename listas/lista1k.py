import random
class lista1k:
    def lista1k(self):
        lista1k = []
        for _ in range(999):
            novo = random.randint(-100,999)
            lista1k.append(novo)
        return lista1k