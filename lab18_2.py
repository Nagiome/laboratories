# Задание 2
# Четыре точки заданы своими координатами X (x1, x2, x3), Y (y1, y2, y3), Z (z1, z2, z3), T(t1,t2, t3). 
# Выяснить, какие из них находятся на минимальном расстоянии друг от друга
# и вывести на экран значение этого расстояния. 
# Вычисление расстояния между двумя точками оформить в виде процедуры. 
# Все результаты представить в файле data.txt.

import math

# Это процедура для вычисления расстояния между двумя точками в 3D пространстве
def distance(point1, point2):
    # Формула расстояния между двумя точками в пространстве
    return math.sqrt(
        (point1[0] - point2[0]) ** 2 +
        (point1[1] - point2[1]) ** 2 +
        (point1[2] - point2[2]) ** 2
    )


# Ввод координат точек пользователем
print("Введите координаты точки X")
x1 = float(input("x1 = "))
x2 = float(input("x2 = "))
x3 = float(input("x3 = "))
X = (x1, x2, x3)

print("\nВведите координаты точки Y")
y1 = float(input("y1 = "))
y2 = float(input("y2 = "))
y3 = float(input("y3 = "))
Y = (y1, y2, y3)

print("Введите координаты точки Z")
z1 = float(input("z1 = "))
z2 = float(input("z2 = "))
z3 = float(input("z3 = "))
Z = (z1, z2, z3)

print("Введите координаты точки T")
t1 = float(input("t1 = "))
t2 = float(input("t2 = "))
t3 = float(input("t3 = "))
T = (t1, t2, t3)

# Список всех точек с их названиями
points = {
    "X": X,
    "Y": Y,
    "Z": Z,
    "T": T
}

# Переменные для хранения минимального расстояния
min_distance = None
closest_points = ()

# Список названий точек
point_names = list(points.keys())

# Перебираем все пары точек
for i in range(len(point_names)):
    for j in range(i + 1, len(point_names)):
        p1_name = point_names[i]
        p2_name = point_names[j]

        # Вычисляем расстояние между текущей парой точек
        dist = distance(points[p1_name], points[p2_name])

        # Если минимальное расстояние ещё не задано
        # или найдено меньшее расстояние
        if min_distance is None or dist < min_distance:
            min_distance = dist
            closest_points = (p1_name, p2_name)

# Записываем результат в файл data.txt
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Минимальное расстояние между точками:\n")
    file.write(f"Точки: {closest_points[0]} и {closest_points[1]}\n")
    file.write(f"Расстояние: {min_distance}\n")

# Вывод результата на экран
print("\nРезультат записан в файл data.txt")
print("Ближайшие точки:", closest_points[0], "и", closest_points[1])
print("Минимальное расстояние:", min_distance)
input("Нажмите Enter, чтобы закрыть...")
