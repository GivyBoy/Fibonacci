
def fibonacci_List(N):
    l = []
    x, y = 0, 1
    while len(l) < N:
        x, y = y, x + y
        l.append(x)
    return l

print(fibonacci_List(23))