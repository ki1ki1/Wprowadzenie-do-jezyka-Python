list = list(range(1, 11))
first_half = list[:5]
second_half = list[5:]
print("Pierwsza połowa: ", first_half)
print("Druga połowa: ", second_half)

#zadanie2
merged_list = [0] + first_half + second_half
copy_of_merged_list = merged_list.copy()
copy_of_merged_list.sort(reverse=True) 
print("Połączona lista: ", merged_list)
print("Kopia połączonej listy posortowana malejąco: ", copy_of_merged_list)