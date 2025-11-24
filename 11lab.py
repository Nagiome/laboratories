from datetime import datetime
import re

# Газеты и их форматы вывода
newspapers = [
    ("The Moscow Times", "%A, %B %d, %Y"),
    ("The Guardian", "%A, %d.%m.%y"),
    ("Daily News", "%A, %d %B %Y")
]
# %A - день недели полностью, %Y - год(ХХХХ), %B - месяц полностью,
# %m - месяц(ХХ), %y - год(ХХ), %d - день(ХХ) 
# Поддерживаемые форматы ввода
input_formats = [
    # d-m-y / m-d-y / y-m-d с любыми разделителями
    "%d.%m.%Y", "%d.%m.%y",
    "%Y.%m.%d",
    "%m.%d.%Y", "%m.%d.%y",

    "%d-%m-%Y", "%d-%m-%y",
    "%Y-%m-%d",
    "%m-%d-%Y", "%m-%d-%y",

    "%d/%m/%Y", "%d/%m/%y",
    "%m/%d/%Y", "%m/%d/%y",
    "%Y/%m/%d",

    "%d\\%m\\%Y", "%d\\%m\\%y",
    "%m\\%d\\%Y", "%m\\%d\\%y",

    # словесные форматы
    "%d %B %Y", "%d %b %Y",
    "%d %B %y", "%d %b %y",

    "%B %d %Y", "%b %d %Y",
    "%B %d, %Y", "%b %d, %Y",

    "%d %B, %Y", "%d %b, %Y"
]

def normalize_date(s: str) -> str:
    """Заменяет все разделители / - \ на точку."""
    return re.sub(r"[\/\\\-]", ".", s)

def parse_date(date_str: str):
    """Пытается разобрать дату по всем форматам, кроме ISO."""
    normalized = normalize_date(date_str)

    for fmt in input_formats:
        try:
            return datetime.strptime(normalized, fmt)
        except ValueError:
            continue

    return None


print("Введите дату (или leave для выхода)\n")

while True:
    raw = input("Дата(день.месяц.год): ").strip()

    if raw.lower() == "leave":
        print("Завершение программы.")
        input("Введите Enter, чтобы выйти из программы")
        break

    try:
        date_obj = parse_date(raw)
        if not date_obj:
            raise ValueError

        for name, output_fmt in newspapers:
            print(f"{name} — {date_obj.strftime(output_fmt)}")
        print()

    except Exception:
        print("Ошибка: введённая дата не распознана.\n")
        continue