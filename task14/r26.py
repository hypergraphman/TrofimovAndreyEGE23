for x in range(0, 15):
    n = 1 * 15 ** 4 + 2 * 15 ** 3 + 3 * 15 ** 2 + x * 15 + 5 + 1 * 15 ** 4 + x * 15 ** 3 + 2 * 15 ** 2 + 3 * 15 + 3
    if n % 14 == 0:
        print(n // 14, x)