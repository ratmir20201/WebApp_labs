counter = {}
filename = input("Enter a file name: ")

with open(filename, 'r') as file:
    for i_line in file:
        if i_line.startswith("Author: "):
            author = i_line[8:-1]
            if author in counter.keys():
                counter[author] += 1
            else:
                counter[author] = 1

max_message = 0
elem = 0
for i in counter:
    if counter[i] > max_message:
        max_message = counter[i]
        elem = i

print(elem, max_message)