def n_to_13(n):
    res = ''
    while n > 0:
        res = '0123456789ABC'[n % 13] + res
        n //= 13
    return res


for x in range(0, 10):
    s1 = 3 * 15**4 + x * 15**3 + 15**2 + 5 * 15 + x
    s2 = (3051 + x * 100)**2 + 2 * (3051 + x * 100) + 3
    s3 = x ** x
    s4 = (103 + x * 10)**2 + x * (103 + x * 10) + 3
    s5 = (x + 1)**2 + x * (x + 1) + 2
    n = s1 + s2 + s3 + s4 + s5
    if n % 13 == 0:
        print(n_to_13(n))
