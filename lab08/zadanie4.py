import csv

with open('zamowienia.csv', newline='', encoding="utf8", errors="ignore") as file:
    reader = csv.reader(file, delimiter=';')
    header = next(reader)
    for i, row in enumerate(reader):
        if i >= 5: 
            break
        record = {header[j]: row[j] for j in range(len(header))}
        print(record)
