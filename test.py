a, b, c = int(input()), int(input()), int(input())
if b <= a <= c or c <= a <= b:
    print(a)
if a <= b <= c or c <= b <= a:
    print(b)
elif (c > a and c < b) or (b < a and c > b) :
    print(c)
