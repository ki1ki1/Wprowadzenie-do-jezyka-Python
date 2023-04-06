def get_n_largest_or_smallest(n, data, is_largest=True):
    if not all(isinstance(i, (int, float)) for i in data):
        raise ValueError('Lista zawiera wartości nie numeryczne')

    sorted_data = sorted(data, reverse=is_largest)
    return sorted_data[:n] if is_largest else sorted_data[:n][::-1]

data = [10, 5, 8, 20, 3]
n_largest = get_n_largest_or_smallest(2, data, is_largest=True)
n_smallest = get_n_largest_or_smallest(3, data, is_largest=False)
print(n_largest)
print(n_smallest) 