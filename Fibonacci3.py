
def fibonacci(N):
    x, y = 0, 1
    for num in range(N):
        x, y = y, x + y
    return x

print(fibonacci(23))
