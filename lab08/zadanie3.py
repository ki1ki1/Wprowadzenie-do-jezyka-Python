import timeit
from collections import deque

def test_deque_append():
    dq = deque()
    for i in range(10000):
        dq.append(i)

def test_deque_appendleft():
    dq = deque()
    for i in range(10000):
        dq.appendleft(i)

def test_list_append():
    l = []
    for i in range(10000):
        l.append(i)

def test_list_insert():
    l = []
    for i in range(10000):
        l.insert(0, i)

print("Czas wykonania 1000 operacji append na deque:", timeit.timeit(test_deque_append, number=1000))
print("Czas wykonania 1000 operacji appendleft na deque:", timeit.timeit(test_deque_appendleft, number=1000))
print("Czas wykonania 1000 operacji append na liście:", timeit.timeit(test_list_append, number=1000))
print("Czas wykonania 1000 operacji insert(0) na liście:", timeit.timeit(test_list_insert, number=1000))
