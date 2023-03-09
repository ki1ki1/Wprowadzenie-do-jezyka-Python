import string

text = input('Wprowadź dowolny tekst: ')

lowercase_chars = set(c for c in text.lower() if c in string.ascii_lowercase)
digits_chars = set(c for c in text if c in string.digits)

lowercase_percent = len(lowercase_chars) / len(text) * 100
digits_percent = len(digits_chars) / len(text) * 100

print(f'Liczba znaków z ascii_lowercase: {len(lowercase_chars)}, czyli {lowercase_percent:.2f}% tekstu.')
print(f'Liczba cyfr: {len(digits_chars)}, czyli {digits_percent:.2f}% tekstu.')