def merge_files(file_list, output_file):
    with open(output_file, 'w') as outfile:
        for file_name in file_list:
            with open(file_name) as infile:
                outfile.write(infile.read())

file_list = ['plik1.txt', 'plik2.txt', 'plik3.txt']
output_file = 'wynik.txt'

merge_files(file_list, output_file)