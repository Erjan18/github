def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2)


x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
print(distance(x1, x2, y1, y2))