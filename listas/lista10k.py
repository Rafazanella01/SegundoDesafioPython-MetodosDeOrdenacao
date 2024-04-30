import random

class lista10k:
    def lista10k(self):
        lista10k = []
        for _ in range(9999):
            novo = random.randint(-100,999)
            lista10k.append(novo)
        return lista10k