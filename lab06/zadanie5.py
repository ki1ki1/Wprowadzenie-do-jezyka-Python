import unidecode

def save_surnames(surnames):
    a_m_file = open('A-M_nazwiska.txt', 'w', encoding='utf-8')
    n_z_file = open('N-Ż_nazwiska.txt', 'w', encoding='utf-8')

    for surname in surnames:
        decoded_surname = unidecode.unidecode(surname).upper()  # usunięcie polskich znaków i zmiana na wielkie litery
        if decoded_surname[0] >= 'A' and decoded_surname[0] <= 'M':
            a_m_file.write(surname + '\n')
        else:
            n_z_file.write(surname + '\n')

    a_m_file.close()
    n_z_file.close()

surnames = ['Kowalski', 'Nowak', 'Żukowski', 'Adamczyk', 'Małysz', 'Niemczyk', 'Piotrowski']
save_surnames(surnames)