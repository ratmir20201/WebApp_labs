my_str = input()

chars = 0
nums = 0
spec_syms = 0
for char in my_str:
    if char.isalpha():
        chars +=  1
    elif char.isdigit():
        nums += 1
    elif not char.isalnum() and not char.isspace():
        spec_syms += 1

print(chars, nums, spec_syms)