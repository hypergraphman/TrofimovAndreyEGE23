from fnmatch import fnmatch

for i in range(2023, 10**8, 2023):
    if fnmatch(str(i), '1*43?8'):
        print(i, i // 2023)
        