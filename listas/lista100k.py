import random
class lista100k:
    def lista100k(self):
        lista100k = []
        for _ in range(99999):
            novo = random.randint(-99999,99999)
            lista100k.append(novo)
        return lista100k
