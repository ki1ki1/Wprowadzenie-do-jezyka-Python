import sys

print("Podaj liczbę:")
number = int(sys.stdin.readline())
digits = []
multipliers = []
current_multiplier = 1

while number > 0:
    digit = number % 10
    digits.append(str(digit))
    multipliers.append(str(current_multiplier))
    number //= 10
    current_multiplier *= 10
multipliers_str = " + ".join(m + "*" + d for m, d in zip(reversed(multipliers), reversed(digits)))
sys.stdout.write(f"Podaną liczbę można zapisać jako: {multipliers_str}")