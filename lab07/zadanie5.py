def sort_dict(d: dict, func):
    sorted_items = sorted(d.items(), key=lambda x: func(x[1]))
    sorted_dict = {}
    for key, value in sorted_items:
        sorted_dict[key] = value

    return sorted_dict

my_dict = {
    'Jakub': [1, 3, 4, 7],
    'Adam': [25],
    'Katarzyna': [9, 10, 11, 12]
}

print(sort_dict(my_dict, min))
print(sort_dict(my_dict, max))
print(sort_dict(my_dict, sum))
print(sort_dict(my_dict, lambda x: abs(min(x))))