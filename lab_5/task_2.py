counter = {}

with open('mbox-short.txt', 'r') as file:
    for i_line in file:
        if i_line.startswith("Author: "):
            author = i_line[8:-1]
            if author in counter.keys():
                counter[author] += 1
            else:
                counter[author] = 1

print(counter)