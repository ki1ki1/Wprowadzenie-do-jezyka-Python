import csv
from datetime import datetime

def convert_date_format(filename: str, indx: int, src_format: str, dst_format: str) -> None:
    with open('zadanie2.csv', newline='', encoding="utf8", errors="ignore") as f:
        with open(f'{filename}.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=";")
            reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
            kolumny = next(reader, None)
            writer.writerow(kolumny)
            for wiersz in reader:
                data = datetime.strptime(wiersz[indx], src_format).strftime(dst_format)
                wiersz[indx] = data
                writer.writerow(wiersz)

convert_date_format("zadanie5", 2, "%Y%m%d", "%Y-%m-%d")


