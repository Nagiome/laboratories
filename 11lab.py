from datetime import datetime
import re

# Газеты и их форматы вывода
newspapers = [
    ("The Moscow Times", "%A, %B %d, %Y"),
    ("The Guardian", "%A, %d.%m.%y"),
    ("Daily News", "%A, %d %B %Y")
]

# Универсальные форматы для считывания дат
input_formats = [
    "%d.%m.%Y",
    "%d.%m.%y",
    "%d.%m.%y",     # подойдёт для 12.10.20
    "%Y.%m.%d",
]

def normalize_date(s: str) -> str:
    """Заменяет любые разделители / \ - на точку."""
    return re.sub(r"[\/\\-]", ".", s)

def parse_date(date_str: str) -> datetime | None:
    """Пытается разобрать дату по универсальным форматам."""
    date_str = normalize_date(date_str)
    for fmt in input_formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            pass
    return None

# Основная логика
for name, output_fmt in newspapers:
    raw = input(f"Введите дату для {name}: ")

    date_obj = parse_date(raw)
    if date_obj:
        # ВЫВОД остаётся тем же, строго по формату газеты
        print(f"{name} - {date_obj.strftime(output_fmt)}")
    else:
        print(f"{name} - Неверный формат даты")
input('Нажмите Enter, чтобы завершить программу')