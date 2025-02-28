import time

def ki_infinito():
    ki = 9000
    while True:
        yield f"Ki do Goku atual {ki}"
        ki += 1000
        time.sleep(0.5)

goku_treino = ki_infinito()

for _ in range(10):
    print(next(goku_treino))
