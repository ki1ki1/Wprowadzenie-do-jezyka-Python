import random

with open("hasla.txt", "r", encoding="utf-8") as file:
    passwords = [line.strip() for line in file]
password = random.choice(passwords)
masked_password = ["_" if sign.isalpha() else sign for sign in password]
print(" ".join(masked_password))
while True:
    answer = input("Podaj litere lub haslo: ").strip()
    if len(answer) == 1:
        if answer.lower() in password.lower():
            for i, znak in enumerate(password):
                if znak.lower() == answer.lower():
                    masked_password[i] = password[i]
            print(" ".join(masked_password))
        else:
            print("Nie ma takiej litery w haśle.")
    elif len(answer) > 1:
        if answer.lower() == password.lower():
            print("Gratulacje, odgadłeś hasło!")
            break
        else:
            print("Nieprawidłowe hasło.")

print("Dziękujemy za udział w grze!")