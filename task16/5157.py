from functools import lru_cache


@lru_cache(None)
def f(n):
    if n >= 10000:
        return n
    if n < 10000 and n % 3 == 0:
        return n + f(n // 3)
    if n < 10000 and n % 3 != 0:
        return 2 * n + f(n + 3)


for i in range(10000, 0, -3):
    f(i)
# for i in range(10000, 0, -1):
#     f(i)

print(f(999) - f(46))