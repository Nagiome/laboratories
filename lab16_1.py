n = int(input("Введите натуральное число: "))

if n <= 0:
    print("Ошибка: число должно быть натуральным")
else:
    print("Подходящие числа:")

    for i in range(1, n + 1):
        temp = i
        ok = True

        while temp > 0:
            digit = temp % 10

            # Если есть цифра 0 — число не подходит
            if digit == 0 or i % digit != 0:
                ok = False
                break

            temp //= 10

        if ok:
            print(i)
input("Нажмите Enter, чтобы закрыть...")