# Электронный журнал с удалением и сортировкой
# Основной словарь:
# ключ — фамилия ученика
# значение — словарь предметов и их оценок
journal = {
    "Сердюк": {"математика": 4, "география": 5},
    "Бортников": {"русский язык": 4, "квантовая физика": 5}
}

# Оценки ученика
def show_marks(name):
    if name in journal:
        print(f"Оценки ученика {name}:")
        # sorted сортирует предметы по алфавиту
        for subject, grade in sorted(journal[name].items()):
            print(f"{subject}: {grade}")
    else:
        print("Ученик не найден.")

# Добавление нового ученика
def add_student(name):
    # setdefault создаёт ученика со значением {} если его нет
    journal.setdefault(name, {})
    print("Ученик добавлен.")

# Удаление ученика
def delete_student(name):
    if name in journal:
        del journal[name]
        print("Ученик удалён.")
    else:
        print("Такого ученика нет.")

# Добавление или изменение предмета
def add_subject(name, subject, grade):
    if name in journal:
        journal[name][subject] = grade
        print("Предмет добавлен/обновлён.")
    else:
        print("Ученик не найден.")

#Удаление предмета
def delete_subject(name, subject):
    if name in journal:
        if subject in journal[name]:
            del journal[name][subject]
            print("Предмет удалён.")
        else:
            print("У ученика нет такого предмета.")
    else:
        print("Ученик не найден.")

# Вывести средний балл всех учеников
def average_all():
    for name in sorted(journal):
        subjects = journal[name]
        if subjects:
            avg = sum(subjects.values()) / len(subjects.values())
            print(f"{name}: средний балл {avg:.2f}")
        else:
            print(f"{name}: нет оценок.")

# Основное меню
while True:
    print("\n1 — Показать оценки ученика")
    print("2 — Добавить/изменить предмет")
    print("3 — Добавить ученика")
    print("4 — Показать средний балл всех")
    print("5 — Удалить предмет")
    print("6 — Удалить ученика")
    print("7 — Выход")

    choice = input("Ваш выбор: ")

    if choice == "1":
        show_marks(input("Фамилия ученика: "))
    elif choice == "2":
        name = input("Фамилия: ")
        subject = input("Предмет: ")
        grade = int(input("Оценка: "))
        add_subject(name, subject, grade)
    elif choice == "3":
        add_student(input("Новый ученик: "))
    elif choice == "4":
        average_all()
    elif choice == "5":
        name = input("Фамилия: ")
        subject = input("Предмет: ")
        delete_subject(name, subject)
    elif choice == "6":
        delete_student(input("Фамилия ученика: "))
    elif choice == "7":
        print("Выход...")
        break
    else:
        print("Ошибка ввода.")