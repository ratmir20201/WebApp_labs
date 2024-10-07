num = int(input())
a = 0
b = 1

for i in range(2, num):
    c = a + b
    print(c, end=' ')
    a = b
    b = c
