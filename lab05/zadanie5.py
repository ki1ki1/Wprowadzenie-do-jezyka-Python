from typing import List, Tuple
from random import randint

def dice_rolls(n: int) -> List[Tuple[str, int]]:
    rolls = []
    for i in range(n):
        result = randint(1, 6)
        count = sum(1 for roll in rolls if roll[0] == f"oczka: {result}")
        rolls.append((f"oczka: {result}", f"rzutów: {count + 1}"))
    return rolls

n = int(input("Podaj liczbę rzutów: "))
results = dice_rolls(n)
print(results)