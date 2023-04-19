from typing import List, Any

def extract_numbers(vals: List[Any]) -> List[int | float]:
    return list(filter(lambda x: isinstance(x, (int, float)), vals))

vals = [1, '2', 3.5, '4.7', 'abc', 5]

numbers = extract_numbers(vals)
print(numbers)