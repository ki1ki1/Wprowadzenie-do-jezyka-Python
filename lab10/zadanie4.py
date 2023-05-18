from datetime import datetime, date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    if today.month == birth_date.month:
        months = 0
        days = today.day - birth_date.day
    elif today.month > birth_date.month:
        months = today.month - birth_date.month
        days = today.day
    else:
        months = 12 - birth_date.month + today.month
        days = today.day

    next_birthday = date(today.year, birth_date.month, birth_date.day)
    if today > next_birthday:
        next_birthday = date(today.year + 1, birth_date.month, birth_date.day)
    days_to_next_birthday = (next_birthday - today).days

    print(f"Dzisiaj masz {age} lat, {months} miesięcy i {days} dni.")
    print(f"Do twoich kolejnych urodzin pozostało {days_to_next_birthday} dni.")

birth_date_str = input("Podaj swoją datę urodzenia w formacie RRRR-MM-DD: ")
birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
calculate_age(birth_date)
