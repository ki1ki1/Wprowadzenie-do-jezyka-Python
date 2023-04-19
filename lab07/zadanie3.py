def sort_list(data, reversed=False):
    str_data = sorted([x for x in data if isinstance(x, str)])
    int_data = sorted([x for x in data if isinstance(x, int)])
    if reversed:
        return str_data + int_data
    else:
        return int_data + str_data

data = [10, 'samochód', 'drzewo', 5, 'jabłko']
print(sort_list(data)) 
print(sort_list(data, reversed=True))