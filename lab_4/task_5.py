num = int(input())
max_num = num
while True:
    num = int(input())
    if num == 0:
        break
    if max_num < num:
        max_num = num
print(max_num)