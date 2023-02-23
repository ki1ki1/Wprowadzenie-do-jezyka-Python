a = 41212
b = int("1010", 2)
print("b: ", b)
c = 4.4
d = float("6.022e23")
print("d: ", d)

print(f"Liczba ustawionych bitów w {a}: ", a.bit_count())
print(f"Liczba {c} jest calkowita?", c.is_integer())

x = 0b1010
y = x << 2 #przesuniecie o 2 pozycje w lewo
print(f"Przesuniecie {x} o 2 pozycje w lewo: ", bin(y))

z = x >> 3 #przesuniecie o 3 pozycje w prawo
print(f"Przesuniecie {x} o 3 pozycje w prawo: ",bin(z))

s = x & y #operacja AND
print("AND: ", bin(s))

w = x | y #operacja OR
print("OR: ", bin(w))

