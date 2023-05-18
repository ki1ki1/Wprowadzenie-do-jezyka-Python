import os
import csv

def merge_txt_to_csv(folder_path, output_file):
    header_written = False
    with open(output_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as txt_file:
                        content = txt_file.readlines()
                        if not header_written:
                            csv_writer.writerow(content[0].strip().split('\t'))
                            header_written = True
                        for line in content[1:]:
                            csv_writer.writerow(line.strip().split('\t'))

folder_path = "data_for_lab_10"
output_file = "zadanie2.csv"

merge_txt_to_csv(folder_path, output_file)
