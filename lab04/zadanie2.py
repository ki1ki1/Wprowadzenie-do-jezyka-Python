value = input("Podaj wartość: ")

try:
    int_value = int(value)
    print(f"{value} może być rzutowana na typ int.")
except ValueError:
    print(f"{value} nie może być rzutowana na typ int.")

try:
    float_value = float(value)
    print(f"{value} może być rzutowana na typ float.")
except ValueError:
    print(f"{value} nie może być rzutowana na typ float.")