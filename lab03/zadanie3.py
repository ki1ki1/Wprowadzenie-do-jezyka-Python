text = input("Podaj dowolny tekst: ")
unique_chars = sorted(set(text.lower()))
print("Unikalne znaki w tekście:", ''.join(unique_chars))