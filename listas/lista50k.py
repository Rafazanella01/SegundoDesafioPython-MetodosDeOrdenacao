import random
class lista50k:
    def lista50k(self):
        lista50k = []
        for _ in range(49999):
            novo = random.randint(-100,999)
            lista50k.append(novo)
        return lista50k