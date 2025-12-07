import os

# база пользователей
users = {
    "admin": "password",
    "": ""   # пустой логин и пароль
}

# словарь для отслеживания оставшихся попыток
attempts = {}

# максимальное число попыток
MAX_ATTEMPTS = 3

while True:
    print("=== МЕНЮ ===")
    print("1 — Регистрация")
    print("2 — Вход")
    print("3 — Выход")
    choice = input("Выберите действие: ")

    # =======================
    #      РЕГИСТРАЦИЯ
    # =======================
    if choice == "1":
        login = input("Введите новый логин: ")

        if login in users:
            print("Такой логин уже существует")
            continue

        new_password = input("Введите новый пароль: ")
        users[login] = new_password  # <-- здесь ошибка была
        attempts[login] = MAX_ATTEMPTS  
        print("Регистрация завершена")

    # =======================
    #         ВХОД
    # =======================
    elif choice == "2":
        login = input("Введите логин: ")
        password = input("Введите пароль: ")

        # если пользователь впервые пытается войти — дать ему попытки
        if login not in attempts:
            attempts[login] = MAX_ATTEMPTS

        # если попытки закончились
        if attempts[login] == 0:
            print("Попыток больше нет. Аккаунт заблокирован.")
            continue

        # проверка логина
        if login in users and users[login] == password:
            print("Добро пожаловать")
            attempts[login] = MAX_ATTEMPTS  # сбросить попытки
        else:
            attempts[login] -= 1
            print(f"Доступ ограничен. Осталось попыток: {attempts[login]}")
            os.startfile("maxwell.gif")

            if attempts[login] == 0:
                print("Аккаунт заблокирован.")

    # =======================
    #         ВЫХОД
    # =======================
    elif choice == "3":
        print("Выход...")
        break

    else:
        print("Команда не распознана.")
