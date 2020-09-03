a, b = 0, 1

c = int(input('Enter how many Fibs you want: '))
e = c - 1
d = []

while True:
    a, b = b, a + b
    if len(d) > e:
        break
    d.append(a)

print(d)




