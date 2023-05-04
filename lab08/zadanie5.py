import random
from array import array
def top_10_percent(arr):
    arr_sorted = sorted(arr, reverse=True)
    top_values_count = round(len(arr) * 0.1)
    return arr_sorted[:top_values_count]

values = array('f', [random.random() for _ in range(100)])
print(top_10_percent(values.tolist()))
