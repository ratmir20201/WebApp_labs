words = []

with open('romeo.txt', 'r') as file:
    for i_line in file:
        words_line = i_line.split()
        for i_word in words_line:
            if i_word not in words:
                words.append(i_word)

words.sort()
print(words)