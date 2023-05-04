from array import array
import random
import datetime

tab_of_floats = array('f', [random.random() for _ in range(1_000_000)])
start = datetime.datetime.now()
with open('floats_array.bin', 'wb') as file_arr:
    tab_of_floats.tofile(file_arr)
end = datetime.datetime.now()
print("Czas zapisu tablicy:", end - start)

start = datetime.datetime.now()
tab_of_floats_loaded = array('f')
file_arr  = open('floats_array.bin', 'rb')
tab_of_floats_loaded.fromfile(file_arr, 1_000_000)
file_arr.close()
end = datetime.datetime.now()
print("Czas wczytywania tablicy:", end - start)

list_of_floats = [random.random() for _ in range(1_000_000)]
start = datetime.datetime.now()
with open('floats_list.txt', 'w') as file_arr:
    file_arr.writelines('\n'.join([str(x) for x in list_of_floats]))
end = datetime.datetime.now()
print("Czas zapisu listy:", end - start)

start = datetime.datetime.now()
with open('floats_list.txt', 'r') as file_list:
    list_of_floats_loaded = file_list.readlines()

list_of_floats_loaded = [float(x.strip()) for x in list_of_floats_loaded]
end = datetime.datetime.now()
print("Czas wczytywania listy:", end - start)

