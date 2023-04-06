def generate_emails(file_name, domain):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open('emails.txt', 'w', encoding='utf-8') as output_file:
        for line in lines:
            name = line.strip().lower().replace(' ', '.')
            name = name.translate(str.maketrans('ąćęłńóśźż', 'acelnoszz'))
            email = f"{name}@{domain}\n"
            output_file.write(f"{line.strip()}, {email}")


generate_emails("names.txt", "student.uwm.edu.pl")