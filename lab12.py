# Словарь сезонов по номеру месяца
seasons = {
    1: "Зима", 2: "Зима", 3: "Весна",
    4: "Весна", 5: "Весна", 6: "Лето",
    7: "Лето", 8: "Лето", 9: "Осень",
    10: "Осень", 11: "Осень", 12: "Зима"
}

# Словарь русских названий месяцев
ru_months = {
    "январь": 1, "февраль": 2, "март": 3, "апрель": 4, "май": 5, "июнь": 6,
    "июль": 7, "август": 8, "сентябрь": 9, "октябрь": 10, "ноябрь": 11, "декабрь": 12
}

# Словарь английских названий месяцев
en_months = {
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12
}

usI = input("Введите номер или название месяца: ").strip().lower()

# 1) Если введено число
if usI.isdigit():
    month = int(usI)
# 2) Если слово — проверяем в словарях
elif usI in ru_months:
    month = ru_months[usI]
elif usI in en_months:
    month = en_months[usI]
else:
    month = None

# Вывод результата
if month in seasons:
    print(seasons[month])
else:
    print("Некорректный номер месяца")
input("Введите Enter, чтобы выйти из программы")