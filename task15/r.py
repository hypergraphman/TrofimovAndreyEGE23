for a in range(1, 100):
    if all((y + 2 * x < a) or (x > 20) or (y > 30) for x in range(1, 100) for y in range(1, 100)):
        print(a)
