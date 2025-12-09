
def is_prime(k: int) -> bool:
    """Проверка простоты числа."""
    if k <= 1:
        return False
    if k <= 3:
        return True
    if k % 2 == 0:
        return False
    i = 3
    while i * i <= k:
        if k % i == 0:
            return False
        i += 2
    return True

def twin_primes_in_interval(n: int):
    """Возвращает список пар (p, p+2) — близнецов в отрезке [n, 2n]."""
    if n <= 2:
        raise ValueError("n должно быть больше 2")
    low, high = n, 2 * n
    twins = []
    for p in range(low, high - 1):
        if is_prime(p) and p + 2 <= high and is_prime(p + 2):
            twins.append((p, p + 2))
    return twins

if name == "main":
    n = int(input("Введите n (натуральное, >2): "))
    pairs = twin_primes_in_interval(n)
    if pairs:
        print("Пары близнецов на отрезке [{}, {}]:".format(n, 2*n))
        for a, b in pairs:
            print(a, b)
    else:
        print("Пары близнецов не найдены в данном отрезке.")