import os

# база пользователей
users = {
    "admin": "password",
    "": ""   #пустой логин и пароль
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

    # регистрация
    if choice == "1":
        new_login = input("Введите новый логин: ")

        if new_login in users:
            print("Такой логин уже существует")
            continue #возвращаем пользователя вначало цикла

        new_password = input("Введите новый пароль: ")
        users[new_login] = new_password
        attempts[new_login] = MAX_ATTEMPTS  # даём 3 попытки новому пользователю
        print("Регистрация завершена")

    # вход
    elif choice == "2":
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        
        if login == "admin" and password == "password": #проверка на логин в адм панель
            print("Добро пожаловать")
        else:
            print("Доступ ограничен")
            os.startfile("maxwell.gif") #открытие гифки кота

        # если пользователь ещё не входил — даем ему 3 попытки
        if login not in attempts:
            attempts[login] = MAX_ATTEMPTS

        # проверка блокировки
        if attempts[login] == 0:
            print("Попыток больше нет.")
            continue

        # проверка логина и пароля

