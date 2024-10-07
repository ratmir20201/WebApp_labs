my_str = "/*Jon is @developer & musician!!"

result = ""
for char in my_str:
    if char.isalnum() or char.isspace():
        result += char
    else:
        result += "#"

print(result)