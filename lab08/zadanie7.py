from collections import Counter, deque
import random
import time

def create_kolo_fortuny(*args):
    counter = Counter(args)
    return deque(counter.elements())

def spinit(ticks: int, kolo: deque):
    waits = [random.uniform(0.1, 0.5) for _ in range(ticks)]
    for i in range(ticks):
        kolo.rotate(-1)
        print(f"Aktualny stan koła: {list(kolo)}")
        time.sleep(waits[i])

        if kolo[0] == wygrana:
            print("Wygrałeś")
            return

    print("Niestety, nie udało się wygrać.")

kolo = create_kolo_fortuny('a', 'b', 'c', 'd', 'e', 'f')
wygrana = random.choice(kolo)

spinit(10, kolo)
