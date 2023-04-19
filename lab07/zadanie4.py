import csv
import datetime

with open('zamowienia.csv', newline='', encoding="utf8", errors="ignore") as file:
    reader = csv.reader(file, delimiter=';',  quoting=csv.QUOTE_NONE)
    header = next(reader, None)
    with open('zamowienia_polska.csv', 'w', encoding='utf-8', newline='') as out_file_polska, \
         open('zamowienia_niemcy.csv', 'w', encoding='utf-8', newline='') as out_file_niemcy:
        writer_polska = csv.writer(out_file_polska, delimiter=';')
        writer_niemcy = csv.writer(out_file_niemcy, delimiter=';')
        writer_polska.writerow(header)
        writer_niemcy.writerow(header)
        for row in reader:
            if row[0] == 'Polska':
                writer_polska.writerow(map(lambda x: datetime.datetime.strptime(x, '%d.%m.%Y').strftime('%Y-%m-%d') if x == row[2] else float(x.replace(',', '.').replace(' ', '').replace(' zł', '').replace('z', '')) if x == row[4] else x, row))
            elif row[0] == 'Niemcy':
                writer_niemcy.writerow(map(lambda x: datetime.datetime.strptime(x, '%d.%m.%Y').strftime('%Y-%m-%d') if x == row[2] else float(x.replace(',', '.').replace(' ', '').replace(' zł', '').replace('z', '')) if x == row[4] else x, row))
