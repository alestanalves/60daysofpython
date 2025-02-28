import time

def numero_infinito():
    num = 0
    while True:
        yield num
        num += 1

gerador = numero_infinito()

for _ in range(1000000000000):
    print(next(gerador))