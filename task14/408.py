def n_to_4(n):
    res = ''
    while n > 0:
        res = '0123'[n % 4] + res
        n //= 4
    return res


mx_zero = 0
find_n = 0
for x in range(0, 32):
    n = 1 * 32**4 + 7 * 32**3 + 9 * 32**2 + x * 32 + 9 + 7 * 128**3 + x * 128**2 + 9 * 128 + 3
    if n_to_4(n).count('0') > mx_zero:
        mx_zero = n_to_4(n).count('0')
        find_n = n_to_4(n)
print(sum(map(int, find_n)))