def f(n):
    if n > 30:
        return n ** 2 + 5 * n + 4
    if n <= 30 and n % 2 == 0:
        return f(n + 1) + 3 * f(n + 4)
    if n <= 30 and n % 2 != 0:
        return 2 * f(n + 2) + f(n + 5)


c = 0
for i in range(1, 1000 + 1):
    s = 0
    d = f(i)
    while d > 0:
        s += d % 10
        d //= 10
    if s == 27:
    # if sum(map(int, str(f(i)))) == 27:
        c += 1
print(c)