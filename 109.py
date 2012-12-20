
doubles = range(2, 42, 2) + [50]
points = range(1, 21) + range(3, 63, 3) + [25] + doubles

def scores(n, i=0):
    if n is 1:
        for point in doubles:
            yield point
    else:
        for i2 in range(i, len(points)):
            point2 = points[i2]
            for point3 in scores(n-1, i2):
                yield point2 + point3

print sum(1 for n in range(1,4) for point in scores(n) if point < 100)
