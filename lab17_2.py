def read_matrix(rows: int, cols: int):
    """
    Считывает matrix из stdin — rows строк, каждая строка содержит cols чисел, разделённых пробелами.
    Пример ввода строки: 1 2 3
    """
    print(f"Введите {rows} строк матрицы, каждая строка содержит {cols} чисел, разделённых пробелом:")
    mat = []
    for i in range(rows):
        parts = input(f"Строка {i+1}: ").strip().split()
        if len(parts) != cols:
            raise ValueError(f"Ожидалось {cols} чисел в строке, получили {len(parts)}")
        row = [float(x) if '.' in x else int(x) for x in parts]
        mat.append(row)
    return mat

def find_max_pos(matrix):
    """Возвращает (max_value, i, j) — значение и координаты первого вхождения максимума."""
    if not matrix or not matrix[0]:
        raise ValueError("Матрица пустая")
    max_val = matrix[0][0]
    max_i = max_j = 0
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val > max_val:
                max_val = val
                max_i, max_j = i, j
    return max_val, max_i, max_j

def swap_max_elements(A, B):
    """Меняет местами максимальные элементы матриц A и B (in-place)."""
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Матрицы должны иметь одинаковый размер")
    _, ai, aj = find_max_pos(A)
    _, bi, bj = find_max_pos(B)
    A[ai][aj], B[bi][bj] = B[bi][bj], A[ai][aj]
    return A, B

if __name__ == "__main__":
    rows = int(input("Введите число строк: "))
    cols = int(input("Введите число столбцов: "))
    print("Ввод матрицы A:")
    A = read_matrix(rows, cols)
    print("Ввод матрицы B:")
    B = read_matrix(rows, cols)

    print("Матрица A до обмена:")
    for r in A: print(r)
    print("Матрица B до обмена:")
    for r in B: print(r)

    A_after, B_after = swap_max_elements(A, B)

    print("Матрица A после обмена:")
    for r in A_after: print(r)
    print("Матрица B после обмена:")
    for r in B_after: print(r)