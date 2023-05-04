from timeit import timeit
import random

setup = """
from array import array
import random
"""
stmt1_int = """
tab_of_ints = array('i', [random.randint(-1000000, 1000000) for _ in range(1_000_000)])
"""
stmt2_int = """
list_of_ints = [random.randint(-1000000, 1000000) for _ in range(1_000_000)]
"""
stmt1_long = """
tab_of_longs = array('q', [random.randint(-1000000, 1000000) for _ in range(1_000_000)])
"""
stmt2_long = """
list_of_longs = [random.randint(-1000000, 1000000) for _ in range(1_000_000)]
"""

print("Tablica int:")
print(timeit(stmt1_int, setup, number=100))
print(timeit(stmt2_int, setup, number=100))

print("Tablica long:")
print(timeit(stmt1_long, setup, number=100))
print(timeit(stmt2_long, setup, number=100))
