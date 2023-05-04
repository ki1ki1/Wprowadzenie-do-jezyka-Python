from collections import Counter, deque

def create_kolo_fortuny(*args):
    counter = Counter(args)
    return deque(counter.elements())

print(create_kolo_fortuny('a', 'b', 'c', 'a', 'b', 'b'))
